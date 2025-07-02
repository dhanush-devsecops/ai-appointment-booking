import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not api_key:
    st.error("❌ GEMINI_API_KEY not found in .env file")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize Gemini model
model = genai.GenerativeModel(model_name="models/gemini-pro")

# Streamlit UI
st.title("🤖 AI Appointment Booking Assistant (Gemini)")
st.write("📅 Book an appointment using natural language.")

prompt = st.text_input("🗓️ What would you like to book? (e.g., July 5 at 10AM)")

if prompt:
    try:
        response = model.generate_content(prompt)
        st.success("✅ Appointment Suggestion:")
        st.write(response.text)
    except Exception as e:
        st.error(f"❌ Gemini error: {e}")

