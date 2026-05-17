from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('FinalReport.pdf')

docs = loader.load()

print(docs[4].page_content)