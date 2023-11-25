import streamlit as st
st.markdown('# Chatbot')
user_prompt = st.chat_input()
if user_prompt: 
    response = f"echo: {user_prompt}"
    st.markdown(response)
