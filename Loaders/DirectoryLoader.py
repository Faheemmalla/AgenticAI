from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books', #folder jisme multiple books haii
    glob='*.pdf', # matlab jitne bhi .pdf wali file shai folder mai aunko load kro
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)