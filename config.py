import streamlit as st

def set_config(title):
    st.set_page_config(
        page_title=title,
        layout="wide",
        initial_sidebar_state="expanded"
    )