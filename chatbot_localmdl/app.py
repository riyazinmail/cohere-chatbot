import streamlit as st
from chatbot import chat

st.title("Local Chatbot")
user_input = st.text_input("You:")
if user_input:
    st.write("Bot:", chat(user_input))

