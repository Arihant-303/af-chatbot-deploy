import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()  

st.title("Chatbot by Arihant")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

question = st.text_input("Ask a question:")

if question:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question
    )

    st.write("Response:", response.output_text)