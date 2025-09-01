import os
from dotenv import load_dotenv
from document_loader import DocumentLoader
from rag_engine import RAGEngine
from ui import launch_ui


def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    docs = DocumentLoader("data/book_summaries.pdf").load()

    rag = RAGEngine(api_key=api_key)
    rag.index_documents(docs)

    launch_ui(rag)


if __name__ == "__main__":
    main()