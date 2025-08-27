# ui.py
import streamlit as st

def launch_ui(rag):
    st.set_page_config(page_title="Smart Librarian RAG Bot")
    st.title("Smart Librarian")

    st.markdown("Ask for a book based on themes. Example: 'I want a book about friendship and magic'.")

    use_hyde = st.checkbox("Enable HyDE Output", value=True)
    question = st.text_input("Describe the kind of book you want:")
    if st.button("Search") and question:
        with st.spinner("Looking for a match..."):
            result = rag.query(question)
            st.subheader("Recommendation")
            st.write(f"**{result['title']}**")
            st.write(result["summary"])
            if use_hyde:
                st.subheader("HyDE Suggestion")
                st.code(result["hyde"])