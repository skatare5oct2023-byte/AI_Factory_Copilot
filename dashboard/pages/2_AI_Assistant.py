import streamlit as st
import sys
from pathlib import Path


# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))


# Import RAG function
from rag.chatbot import ask_ai


# Page configuration
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)


# Title
st.title("🤖 AI Factory Assistant")

st.write(
    "Ask questions about factory SOPs, maintenance, safety, "
    "and EV battery manufacturing."
)


# Question input
question = st.text_input(
    "Ask the AI Assistant"
)


# Ask AI button
if st.button("Ask AI"):

    if question:

        with st.spinner("AI is analyzing factory documents..."):

            try:
                # Call RAG + Ollama
                answer = ask_ai(question)

                st.success("Answer generated!")

                st.subheader("🤖 AI Response")

                st.write(answer)

            except Exception as e:

                st.error("Error connecting to AI Assistant")
                st.exception(e)

    else:
        st.warning("Please enter a question.")