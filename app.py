import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini model
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Function to get response from Gemini
def ask_agent(user_input):
    prompt = f"You: {user_input}\nAssistant:"
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Gemini Chat", page_icon="🤖")
st.title("🤖 Gemini Chatbot")
st.write("Ask anything, and Gemini will reply!")

# Input box
user_input = st.text_input("You:", key="input")

if user_input:
    try:
        reply = ask_agent(user_input)
        st.markdown("**Assistant:**")
        st.success(reply)
    except Exception as e:
        st.error(f"Error: {e}")
