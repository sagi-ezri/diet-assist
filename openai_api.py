import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_recommendation(first_name, age, diet_type, diet_goal, allergies, exercise_routine, food_item):
    system_message = {
        "role": "system",
        "content": "You are a persuasive health coach with extensive experience in weight loss, muscle building, and dietary advice, especially within the Israeli community. Your tone is friendly, encouraging, and highly convincing."
    }

    user_message = {
        "role": "user",
        "content": (
            f"{first_name}, a {age}-year-old following a {diet_type} diet with the goal of {diet_goal}, has taken a picture of a food item they want to eat. "
            f"The image contains {food_item}. {first_name} is allergic to {allergies}. They have a regular exercise routine which includes {exercise_routine}. "
            "As their coach and nutrition advisor, advise whether they should eat this or not. Be persuasive, without mentioning their personal reasons for dieting. "
            "Keep your response to two sentences, and suggest a healthier alternative if necessary. Make sure your tone is friendly and informal."
        )
    }

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[system_message, user_message],
            max_tokens=100,
            temperature=0.7,
            n=1,
            stop=None,
        )
        recommendation = response.choices[0].message['content'].strip()
    except Exception as e:
        recommendation = f"Error generating recommendation: {e}"
    
    return recommendation
