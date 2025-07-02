import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env (optional but good practice)
load_dotenv()

# You can also directly use your API key here
api_key = os.getenv("GROQ_API_KEY") 
# Initialize GROQ client
client = Groq(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="🧠 AI Appointment Booking Assistant", page_icon="📅")
st.title("📅 AI Appointment Booking Assistant")
st.write("Book appointments using natural language with GROQ Mixtral AI.")

# User input
prompt = st.text_input("🗓️ What would you like to book? (e.g., 'Book meeting with John on July 5 at 10 AM')")

# Response
if prompt:
    with st.spinner("Thinking..."):
        try:
            chat_completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that helps users schedule appointments."},
                    {"role": "user", "content": prompt},
                ]
            )
            st.success("✅ AI Response:")
            st.write(chat_completion.choices[0].message.content)
        except Exception as e:
            st.error(f"❌ Error: {e}")

