from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

DOCUMENT_FOLDER = Path("data/documents")


def load_documents():
    documents = []

    for pdf_file in DOCUMENT_FOLDER.glob("*.pdf"):
        print(f"Loading: {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))
        docs = loader.load()

        for doc in docs:
            doc.metadata["source"] = pdf_file.name

        documents.extend(docs)

    print(f"\nTotal pages loaded: {len(documents)}")

    return documents


if __name__ == "__main__":
    docs = load_documents()

    for doc in docs[:3]:
        print(doc.page_content[:500])