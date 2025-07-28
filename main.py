import google.generativeai as genai
import os
from dotenv import load_dotenv
from agent import runcontextwrapper

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def ask_agent(user_input):
    prompt = f"You: {user_input}\nAssistant:"
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting chat...")
            break
        try:
            reply = ask_agent(user_input)
            print("Assistant:", reply)
        except Exception as e:
            print("Error:", e)
