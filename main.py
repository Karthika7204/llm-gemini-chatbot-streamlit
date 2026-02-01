import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load env
load_dotenv()

st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="centered",
)

# API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Create client
client = genai.Client(api_key=GOOGLE_API_KEY)

MODEL_NAME = "gemini-2.5-flash"

st.title("🤖 Gemini Chatbot")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_prompt = st.chat_input("Ask Gemini...")
if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.messages.append(
        {"role": "user", "content": user_prompt}
    )

    # Gemini response
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_prompt
    )

    assistant_reply = response.text

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )
