import os
import streamlit as st
from groq import Groq

# ✅ Get API key from Streamlit secrets (set in deployment settings)
api_key = os.environ.get("GROQ_API_KEY")

# ✅ Stop if API key is missing
if not api_key:
    st.error("❌ GROQ_API_KEY not set. Please set it in Streamlit secrets.")
    st.stop()

# ✅ Initialize Groq client
client = Groq(api_key=api_key)

# ✅ Streamlit UI
st.set_page_config(page_title="🧠 AI Appointment Booking Assistant", page_icon="📅")
st.title("📅 AI Appointment Booking Assistant")
st.write("Book appointments using natural language with GROQ's LLaMA3 model.")

# ✅ Input from user
prompt = st.text_input("🗓️ What would you like to book? (e.g., 'Book meeting with John on July 5 at 10 AM')")

# ✅ Handle response
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

