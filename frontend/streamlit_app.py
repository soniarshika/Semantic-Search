import streamlit as st
import requests

st.title("Semantic Search Frontend")

# Input for user query
query = st.text_input("Enter your search query:")

# Button to trigger the search
if st.button("Search"):
    # Make a request to the FastAPI endpoint
    response = requests.get(f"http://localhost:8000/api/search?query={query}")
    
    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()["results"]
        st.write("Search Results:")
        st.write(results)
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
