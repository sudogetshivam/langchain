from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 intresting facts about {topic}',
    input_variables=['topic']
)

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

parser = StrOutputParser()

chain = prompt | model | parser #also know as langchain expression language

result = chain.invoke({'topic':'football'})

print(result)

chain.get_graph().print_ascii() #for visulizing