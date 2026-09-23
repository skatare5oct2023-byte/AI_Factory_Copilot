from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama


# =====================================
# PROJECT PATHS
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_PATH = BASE_DIR / "chroma_db"


# =====================================
# LOAD EMBEDDING MODEL
# =====================================

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =====================================
# LOAD CHROMADB
# =====================================

print("Loading ChromaDB...")

vector_db = Chroma(
    persist_directory=str(CHROMA_PATH),
    embedding_function=embeddings
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)


# =====================================
# LOAD OLLAMA LLM
# =====================================

print("Loading Ollama LLM...")

llm = ChatOllama(
    model="llama3.2",
    temperature=0.2
)


# =====================================
# AI FUNCTION
# =====================================

def ask_ai(question):
    """
    Search factory documents and generate an answer using Ollama.
    """

    # Retrieve relevant documents from ChromaDB
    documents = retriever.invoke(question)

    # Combine retrieved document content
    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    # Create prompt
    prompt = f"""
You are an AI Factory Operations Copilot for EV Battery Manufacturing.

Answer the user's question using ONLY the information provided
in the factory documents.

If the answer is not available in the documents, say:
"I could not find this information in the factory documents."

FACTORY DOCUMENTS:
{context}

USER QUESTION:
{question}

Give a clear, practical, and concise answer for a factory operator.
"""

    # Generate answer using Ollama
    response = llm.invoke(prompt)

    return response.content


# =====================================
# TERMINAL CHAT
# =====================================

if __name__ == "__main__":

    print("\n====================================")
    print(" AI FACTORY OPERATIONS COPILOT ")
    print(" Type 'exit' to stop")
    print("====================================\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            print("AI: Goodbye! Stay safe.")
            break

        answer = ask_ai(question)

        print("\nAI:", answer)
        print()