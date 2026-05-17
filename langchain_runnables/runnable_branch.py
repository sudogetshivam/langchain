from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv
import os

load_dotenv()

prompt1 = PromptTemplate(
template='Write a detailed report on {topic}',
input_variables=['topic' ]
)

prompt2 = PromptTemplate(
template='Summarize the following text in 5 bullet points \n {text}',
input_variableÏs=['text']
)

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.4
)

def word_counter(text):
    return len(text.split())

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>2000 , RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)
result = final_chain.invoke({'topic':'Russia vs Ukraine'})
print(result)
