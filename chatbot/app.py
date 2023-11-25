import streamlit as st
st.markdown('# Chatbot')
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.markdown(message)

user_prompt = st.chat_input()

if user_prompt: 
    st.markdown(f"user: {user_prompt}")
    st.session_state.messages.append(f"user: {user_prompt}")
    response = f"robot: {user_prompt}"    
    st.markdown(response)
    st.session_state.messages.append(response)

