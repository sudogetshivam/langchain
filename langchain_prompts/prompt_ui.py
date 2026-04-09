from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os

import streamlit as st

load_dotenv()

st.header('Research Tool')
user_input = st.text_input('Enter Your prompt')

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

#this is static promp
messages = [
    SystemMessage(content = "You are a helpful assistant"),
    HumanMessage(content=str(user_input))
]

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)