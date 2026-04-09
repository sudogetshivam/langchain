from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os
from langchain_core.prompts import PromptTemplate, load_prompt

import streamlit as st

load_dotenv()


st.header('Research Tool')

paper_input = st.selectbox("Select Research Name",["Attentation is all you need","BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: Language Models are few-shot learners","Diffusion Models can beat GANs or Image Synthesis"])

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical",
"Code-Oriented", "Mathematical"] )

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

#fill the placeholders
# prompt = template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':length_input
# })


model = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.4
)



if st.button('Summarize'):
    # result = model.invoke(prompt)
    #you see we are invoking two times on at here and one at template.invoke, we can minimise it

    chain = template | model
    result = chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
    }) #phele template invoke hua, toh wahi template wala chiz model ke invoke main chalagaya

    st.write(result.content)