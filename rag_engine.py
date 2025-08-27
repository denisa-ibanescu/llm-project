import chromadb
from openai import OpenAI
from chromadb.config import Settings
from hyde_generator import HyDEGenerator

class RAGEngine:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.hyde = HyDEGenerator(api_key)
        self.db = chromadb.Client(Settings())
        self.collection = self.db.get_or_create_collection("book_summaries")
        self.docs = []

    def index_documents(self, docs):
        self.docs = docs
        for i, doc in enumerate(docs):
            themes_str = ", ".join(map(str, doc.get("themes", [])))

            emb = self.client.embeddings.create(
                input=[doc["summary"]],
                model="text-embedding-3-small"
            ).data[0].embedding

            self.collection.add(
                documents=[doc["summary"]],
                embeddings=[emb],  
                metadatas=[{"title": doc["title"], "themes": themes_str}],
                ids=[str(i)],
            )

    def get_summary_by_title(self, title: str) -> str:
        for doc in self.docs:
            if doc["title"].lower() == title.lower():
                return doc["summary"]
        return "Rezumatul nu a fost găsit."

    def query(self, question: str):
        embedding = self.client.embeddings.create(
            input=[question], model="text-embedding-3-small"
        ).data[0].embedding

        results = self.collection.query(query_embeddings=[embedding], n_results=1)
        metadata = results["metadatas"][0][0]
        matched_summary = results["documents"][0][0]
        title = metadata["title"]
        hyde = self.hyde.generate_hypothetical_answer(question)
        return {"title": title, "summary": matched_summary, "hyde": hyde}
