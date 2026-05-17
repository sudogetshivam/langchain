from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv
import os

load_dotenv()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(docs[0])
print(type(docs[0]))

prompt = PromptTemplate(
    template='Write a summary for the following poem \n {poem}',
    input_variables=['poem']
)

parser= StrOutputParser()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

chain = prompt | model | parser
summary = chain.invoke({'poem':docs[0].page_content})
print(summary)