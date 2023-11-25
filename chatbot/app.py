import streamlit as st
from llm import converse

st.markdown('# Chatbot')
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    name = 'user' if message['role'] == 'user' else 'assistant'
    with st.chat_message(name):
        st.markdown(message['content'])

user_prompt = st.chat_input()

if user_prompt: 
    with st.chat_message('user'):
        st.markdown(user_prompt)
    st.session_state.messages.append({'role':'user', 'content': user_prompt})
    response = converse(st.session_state.messages) 
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({'role':'assistant', 'content': response})

