import streamlit as st
from PIL import Image
from image_processing import transform_image
from model import classify_image
from openai_api import get_recommendation
from utils import is_food_detected
from gtts import gTTS


def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("recommendation.mp3")
    return "recommendation.mp3"

def get_audio_player(audio_file):
    audio_file = open(audio_file, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')


def main():
    st.title("🍽️ Personalized Diet Assist App")
    
    st.header("User Information")
    first_name = st.text_input("First Name", "Noam")
    age = st.number_input("Age", min_value=1, max_value=100, value=33)
    diet_type = st.selectbox("Diet Type", ["Vegetarian", "Vegan", "Keto", "Paleo", "Low-Carb", "Mediterranean", "Other"], index=0)
    diet_goal = st.text_input("Diet Goals", "Low carb and muscle build-up")
    allergies = st.text_input("Allergies", "None")
    exercise_routine = st.text_input("Exercise Routine", "Regular weight training")

    st.write("Upload an image, and we'll detect if there's food, identify it, and recommend whether you should eat it based on your dietary preferences.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        with st.spinner('Analyzing image...'):
            input_tensor = transform_image(image)
            predicted_label = classify_image(input_tensor)

        st.write(f"**Detected Object:** {predicted_label}")

        if is_food_detected(predicted_label):
            st.success("🍔 Food detected in the image!")
            with st.spinner('Generating recommendation...'):
                recommendation = get_recommendation(first_name, age, diet_type, diet_goal, allergies, exercise_routine, predicted_label.replace('_', ' '))
            
            st.write(f"**Recommendation:** {recommendation}")
            
            audio_file = text_to_speech(recommendation)
            
            get_audio_player(audio_file)
        else:
            st.warning("🚫 No recognizable food detected in the image.")

if __name__ == "__main__":
    main()
