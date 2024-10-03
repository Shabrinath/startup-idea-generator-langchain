import streamlit as st
import langchain_helper

st.title("Startup Idea Generator")

domain = st.sidebar.selectbox("Pick a Domain", ("Health", "Education", "Finance", "Travel", "Food", "Retail", "RealEstate"))

if domain:
    response = langchain_helper.generate_startup_name_and_items(domain)
    st.write("**Startup Name:**")
    st.header(response['startup_name'].strip())
    startup_items = response['startup_items']
    st.write("**Startup Description:**")
    st.write(startup_items)

