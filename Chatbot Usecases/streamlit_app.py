import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# 🌱 Load environment variables
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

# 🔐 Validate API key
if not api_key:
    st.error("Cohere API key not found. Please check your .env file.")
    st.stop()

# 🤖 Initialize Cohere client
co = cohere.Client(api_key)

# 🖼️ Page configuration
st.set_page_config(page_title="Cohere Chatbot", layout="centered")
st.title("💬 Chat with Cohere")

system_message = {
    "role": "SYSTEM",
    "message": "You are a helpful assistant named CohereBot. Always reply in a friendly and concise tone."
}

# 📦 Session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 🧠 Handle user input
def handle_input():
    user_input = st.session_state.user_input.strip()
    if user_input:
        # Save user message
        st.session_state.chat_history.append(("You", user_input))

        try:
            # Call Cohere API
            response = co.chat(
                message=user_input,
                model="command-r",
                temperature=0.7,
                max_tokens=100,
                chat_history = [system_message] + [
                {"role": "USER", "message": msg} if sender == "You" else {"role": "CHATBOT", "message": msg}
                for sender, msg in st.session_state.chat_history
            ]
            )
            bot_reply = response.text.strip()
        except Exception as e:
            bot_reply = f"⚠️ Error: {str(e)}"

        # Save bot response
        st.session_state.chat_history.append(("Bot", bot_reply))

        # Clear input
        st.session_state.user_input = ""

# 📜 Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")

# 📝 Input box
st.text_input("Type your message:", key="user_input", on_change=handle_input)


