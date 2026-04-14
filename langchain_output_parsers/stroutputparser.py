from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

#1st prompt
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)


#2nd prompt
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. \n {text}",
    input_variables=['text']
)

# prompt1 = template1.invoke({'topic':'black hole'})
# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'text':result.content})
# result = model.invoke(prompt2)

# print(result.content)

parser =  StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'black hole'})

print(result)