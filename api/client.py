import streamlit as st
import requests

st.title('Chatbot Application')
ask=st.chat_input("Ask chatbot...")

def interacts_with_llm(ask):
    response=requests.post(
        'http://localhost:8500/chat/invoke',
        json={
            'input':{
                'prompts':ask
            }
        }
    )

    if response.status_code!=200:
        return f'Error {response.status_code} : {response.text}'

    return response.json()['output']['content']

if ask:

    #user message
    with st.chat_message('user'):
        st.write(ask)
    #response from AI
    with st.chat_message('assistant'):
        with st.spinner('thinking...'):
            response=interacts_with_llm(ask)

        st.write(response)    