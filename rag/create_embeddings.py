from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
load_dotenv()

DOCUMENT_FOLDER = Path("data/documents")

documents = []

for pdf_file in DOCUMENT_FOLDER.glob("*.pdf"):
    print("Processing:", pdf_file.name)

    loader = PyPDFLoader(str(pdf_file))
    docs = loader.load()

    for doc in docs:
        doc.metadata["source"] = pdf_file.name

    documents.extend(docs)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print("Total documents:", len(documents))
print("Total chunks:", len(chunks))

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

print("Embeddings model ready.")