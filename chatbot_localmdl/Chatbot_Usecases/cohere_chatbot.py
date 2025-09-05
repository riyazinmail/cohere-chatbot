import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

# Page config
st.set_page_config(page_title="Cohere Chatbot", layout="centered")
st.title("🤖 Cohere Chatbot")


# Callback function to handle input
def handle_input():
    user_input = st.session_state.user_input
    if user_input:
        # Display user message
        st.markdown(f"**You:** {user_input}")

        # Call Cohere API
        response = co.chat(
            message=user_input,
            model="command-r",
            temperature=0.7,
            max_output_tokens=50  # 👈 restricts bot response length
        )

        # Display bot response
        st.markdown(f"**Bot:** {response.text}")

        # Clear input safely
        st.session_state.user_input = ""

        tokens_used = co.tokenize(text=response.text).tokens
        print("Response token count:", len(tokens_used))

# Input box with callback
st.text_input("Type your message:", key="user_input", on_change=handle_input)

