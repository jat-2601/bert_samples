import streamlit as st
from summarizer import Summarizer
import requests
from bs4 import BeautifulSoup

# Function to summarize text using BERT model
def summarize_text(text):
    bert_model = Summarizer()
    summary = ''.join(bert_model(text, min_length=60))
    return summary

# Function to fetch and summarize text from a URL
def summarize_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    return summarize_text(text)

# Streamlit UI
st.title("Text Summarization Dashboard")

# Text input option
st.header("Summarize Text")
user_input = st.text_area("Enter text to summarize:")
if st.button("Summarize Text"):
    if user_input:
        summary = summarize_text(user_input)
        st.write("Summary:")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

# URL input option
st.header("Summarize URL")
url_input = st.text_input("Enter URL to summarize:")
if st.button("Summarize URL"):
    if url_input:
        summary = summarize_url(url_input)
        st.write("Summary:")
        st.write(summary)
    else:
        st.write("Please enter a valid URL to summarize.")
