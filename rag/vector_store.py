from pathlib import Path

from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENT_FOLDER = BASE_DIR / "data" / "documents"
CHROMA_PATH = BASE_DIR / "chroma_db"


# --------------------------------------------------
# 1. Load PDF documents
# --------------------------------------------------

pdf_files = list(DOCUMENT_FOLDER.glob("*.pdf"))

print(f"Found {len(pdf_files)} PDF documents.")

documents = []

for pdf_file in pdf_files:

    print(f"Loading: {pdf_file.name}")

    loader = PyPDFLoader(str(pdf_file))
    docs = loader.load()

    for doc in docs:
        doc.metadata["source"] = pdf_file.name

    documents.extend(docs)


print(f"Total pages loaded: {len(documents)}")


# --------------------------------------------------
# 2. Split documents into chunks
# --------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Total chunks created: {len(chunks)}")


# --------------------------------------------------
# 3. Create FREE local embeddings
# --------------------------------------------------

print("\nLoading local embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded.")


# --------------------------------------------------
# 4. Create Chroma vector database
# --------------------------------------------------

print("\nCreating Chroma vector database...")

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=str(CHROMA_PATH)
)


# --------------------------------------------------
# 5. Finished
# --------------------------------------------------

print("\n===================================")
print("RAG VECTOR DATABASE CREATED!")
print("===================================")

print(f"PDF documents : {len(pdf_files)}")
print(f"Pages         : {len(documents)}")
print(f"Chunks        : {len(chunks)}")
print(f"Database      : {CHROMA_PATH}")

print("\nYour factory documents are now searchable!")