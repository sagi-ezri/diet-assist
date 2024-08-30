import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_recommendation(food_item):
    system_message = {
        "role": "system",
        "content": "You are a persuasive health coach with extensive experience in weight loss, especially within the Israeli community. Your tone is friendly, encouraging, and highly convincing."
    }


    user_message = {
        "role": "user",
        "content": f"Avital, a 34-year-old mother of two, is on a low-calorie, low-carb diet to lose weight after childbirth. She has taken a picture of something she wants to eat, which is {food_item}. As her coach and nutrition advisor, advise her whether to eat this or not. Be persuasive, without mentioning her personal reasons for dieting. Keep your response to two sentences, and suggest a healthier alternative if necessary. Make sure your tone is friendly and informal."
    }


    try:
        # Use the chat completion endpoint
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
