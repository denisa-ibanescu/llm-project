
# Smart Librarian – RAG + ChromaDB + GPT

This project is an AI-powered book recommender using OpenAI and ChromaDB for Retrieval-Augmented Generation (RAG). It provides book recommendations based on user themes and queries, with a simple Streamlit UI.

---

## Features
- Recommend books based on user themes and context
- Uses `book_summaries.pdf` as the knowledge base
- Embeds book summaries using OpenAI embeddings
- Stores and searches using **ChromaDB** (local vector DB)
- Integrates **HyDE (Hypothetical Answer Generator)** for creative suggestions
- Tool function `get_summary_by_title(title)` to retrieve full book details
- Simple **Streamlit UI** for interaction

---

## Project Structure
```
llm-project/
├── main.py                # Entry point for the Streamlit app
├── document_loader.py     # Loads and parses book summaries from PDF
├── rag_engine.py          # RAG engine for semantic search and retrieval
├── hyde_generator.py      # Generates hypothetical answers using OpenAI
├── ui.py                  # Streamlit UI logic
├── requirements.txt       # Python dependencies
├── data/
│   └── book_summaries.pdf # PDF file with book summaries
```

---

## Requirements
- Python 3.8+
- See `requirements.txt` for all dependencies

---


## Example Questions
- I want a book about freedom and social control.
- What do you recommend for someone who loves war stories?
- I like themes of friendship and adventure.
- What is 1984?

---

## Deliverables
- `book_summaries.pdf` (10+ book summaries)
- Full Python source code with modules
- ChromaDB-based RAG pipeline
- HyDE tool
- Streamlit UI
- Tool: `get_summary_by_title`

---

## Notes
- Assignment requirements: [Assignment-EssentialsOfLLM.pdf](Assignment-EssentialsOfLLM.pdf)
- Summary database: [book_summaries.pdf](book_summaries.pdf)

## Credits
- Built with OpenAI, ChromaDB, and Streamlit.
