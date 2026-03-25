# "Selenium" allows us to automate a web browser so we can actually navigate to a webpage
from scrape import scrape_website, extra_body_content, split_dom_content, clean_body_content
import streamlit as st

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")

    result = scrape_website(url)
    body_content = extra_body_content(result)
    clean_content = clean_body_content(body_content)

    st.session_state_dom_scrape = clean_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", clean_content, height=300)