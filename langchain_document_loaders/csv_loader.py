from langchain_community.document_loaders import TextLoader, WebBaseLoader, CSVLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv
import os

load_dotenv()

url = 'https://medium.com/@dwgray/a-very-simple-website-back-to-the-basics-1dffdc43d19b'

loader = CSVLoader(file_path='results.csv')

docs = loader.load()

print(docs[0].page_content)
print(len(docs))

# prompt = PromptTemplate(
# template='Answer the following question \n {question} from the following text - \n {text}',
# input_variables=['question', 'text']
# )

# parser= StrOutputParser()

# model = ChatGroq(
#     model = "llama-3.3-70b-versatile",
#     groq_api_key = os.getenv("GROQ_API_KEY"),
#     temperature=0.4
# )

# chain = prompt | model | parser
# result = chain.invoke({'question':'What is this page about?','text':docs[0].page_content})
# print(result)