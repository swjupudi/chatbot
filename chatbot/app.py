import streamlit as st
from llm import converse

st.markdown('# Chatbot')
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.markdown(message)

user_prompt = st.chat_input()

if user_prompt: 
    st.markdown(f"user: {user_prompt}")
    st.session_state.messages.append({'role':'user', 'content': user_prompt})
    response = f"robot: {converse(st.session_state.messages)}"   
    st.markdown(response)
    st.session_state.messages.append({'role':'assistant', 'content': response})

