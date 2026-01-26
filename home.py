import streamlit as st
from config import set_config
from utils import create_wordcloud

def create_home_page():
    page_title = "Home"
    set_config(
        title=page_title,
    )

    col1, col2 = st.columns([4, 6])
    with col2:
        st.header(
        "Welcome to My Portfolio",
        divider="green"
        )
        st.markdown(
            """
            Feel free to explore the different sections of my portfolio using the sidebar, including:
        """
        )

        page_links = {
            "About me": "pages/about_me.py",
            "Experience": "pages/experience.py",
            "Personal projects": "pages/personal_projects.py"
        }

        with st.container():
            for page_name, page_path in page_links.items():
                st.page_link(
                    page_path,
                    label=page_name
                )
    
    with col1:
        create_wordcloud()

if __name__ == "__main__":
    create_home_page()