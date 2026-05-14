from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

prompt1 = PromptTemplate(
    template='Genrate a report on this {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Genrate a 5 line summary on this {content}',
    input_variables=['content']
)

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

parser = StrOutputParser()

chain1 = prompt1 | model |  parser
result1 = chain1.invoke({'topic':'Hanta virus'})
chain2 = prompt2 | model | parser
result2 = chain2.invoke({'content':result1})

#shotcut way
chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic':'Lenevo LOQ 15RX9'})

print(result)

chain.get_graph().print_ascii()
