from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama


# ==========================================
# PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_PATH = BASE_DIR / "chroma_db"


# ==========================================
# LOAD EMBEDDING MODEL
# ==========================================

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ==========================================
# LOAD CHROMADB
# ==========================================

print("Loading ChromaDB...")

vector_db = Chroma(
    persist_directory=str(CHROMA_PATH),
    embedding_function=embeddings
)


# Create retriever
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)


# ==========================================
# LOAD OLLAMA LLM
# ==========================================

print("Loading Ollama LLM...")

llm = ChatOllama(
    model="llama3.2",
    temperature=0.3
)


print("\n🏭 AI Factory Operations Copilot Started!")
print("Ask questions about EV battery manufacturing.")
print("Type 'exit' to stop.\n")


# ==========================================
# CHAT LOOP
# ==========================================

while True:

    question = input("Operator: ")

    # Exit condition
    if question.lower() == "exit":
        print("\nAI Factory Copilot stopped.")
        break

    try:

        # Retrieve relevant documents
        documents = retriever.invoke(question)

        # Combine document content
        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        # Create prompt
        prompt = f"""
You are an AI Factory Operations Copilot for EV Battery Manufacturing.

Your job is to help factory operators with questions about:

- Battery production
- Machine maintenance
- Machine troubleshooting
- Factory safety
- Quality control
- Standard Operating Procedures

Use the FACTORY DOCUMENTATION below to answer the question.

FACTORY DOCUMENTATION:
{context}

OPERATOR QUESTION:
{question}

Instructions:
1. Give a clear and practical answer.
2. Use the provided factory documentation.
3. Do not invent information.
4. If the answer is not available in the documentation, say:
   "I could not find this information in the available factory documents."
5. Keep the answer easy for a factory operator to understand.

AI ANSWER:
"""

        # Generate answer using Ollama
        response = llm.invoke(prompt)

        print("\n🤖 AI Assistant:")
        print(response.content)
        print("\n" + "-" * 60 + "\n")

    except Exception as e:

        print("\n❌ Error:")
        print(e)
        print()