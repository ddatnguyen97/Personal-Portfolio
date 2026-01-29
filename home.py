import streamlit as st
from config import set_config
from utils import create_wordcloud
from openpanel.setup import load_openpanel
from openpanel.event_tracking import track_page

import os
from dotenv import load_dotenv

load_dotenv()

def create_home_page():
    if "op_loaded" not in st.session_state:
        load_openpanel(os.getenv["OPENPANEL_CLIENT_ID"])
        st.session_state.op_loaded = True

    if "page_tracked" not in st.session_state:
        track_page("home")
        st.session_state.page_tracked = True

    page_title = "Home"
    set_config(
        title=page_title,
    )

    load_openpanel(os.getenv("OPENPANEL_CLIENT_ID"))

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
        st.markdown("- About me")
        st.markdown("- Experience")
        st.markdown("- Personal projects")

        # page_links = {
        #     "About me": "pages/about_me.py",
        #     "Experience": "pages/experience.py",
        #     "Personal projects": "pages/personal_projects.py"
        # }

        # with st.container():
        #     for page_name, page_path in page_links.items():
        #         st.page_link(
        #             page_path,
        #             label=page_name
        #         )
    
    with col1:
        create_wordcloud()

if __name__ == "__main__":
    create_home_page()