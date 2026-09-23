from fastapi import FastAPI
from pydantic import BaseModel

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

from pathlib import Path


app = FastAPI(
    title="AI Factory Operations Copilot API",
    version="1.0"
)


class Question(BaseModel):
    question: str


# Project path
BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_PATH = BASE_DIR / "chroma_db"


# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Load ChromaDB
vector_db = Chroma(
    persist_directory=str(CHROMA_PATH),
    embedding_function=embeddings
)


# Create retriever
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)


# Load Ollama LLM
llm = ChatOllama(
    model="llama3.2",
    temperature=0.3
)


@app.get("/")
def home():

    return {
        "message": "AI Factory Operations Copilot API Running"
    }


@app.post("/chat")
def chat(data: Question):

    # Search relevant documents
    documents = retriever.invoke(data.question)

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    # Create AI prompt
    prompt = f"""
You are an AI Factory Operations Copilot for EV Battery Manufacturing.

Answer the operator's question using the factory documentation below.

FACTORY DOCUMENTATION:

{context}

OPERATOR QUESTION:

{data.question}

Give a clear, practical, and safe answer.
If the information is not available in the documentation, clearly say so.
"""

    # Ask LLM
    response = llm.invoke(prompt)

    return {

        "question": data.question,

        "answer": response.content

    }