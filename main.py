# "Selenium" allows us to automate a web browser so we can actually navigate to a webpage
from scrape import scrape_website
import streamlit as st

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    print(result)