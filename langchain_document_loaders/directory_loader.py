from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'mypdfs',
    glob= '*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

# print(len(docs))

# print(docs[1].metadata)

for d in docs:
    print(d.metadata)