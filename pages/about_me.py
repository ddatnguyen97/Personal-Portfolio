import streamlit as st
from config import set_config
from utils import get_base64_image, create_social_links, create_spacer, create_logo_holder, create_copy_box
from openpanel.event_tracking import track_event, track_page

import os
from dotenv import load_dotenv

load_dotenv()

def create_about_me_page():
    if "tracked_about" not in st.session_state:
        track_page("About Me")
        st.session_state.tracked_about = True

    page_titile = "About Me"
    set_config(
        title=page_titile,
    )

    profile_img = get_base64_image("assets/images/nhqd_img.jpg")

    linkedin_logo = get_base64_image("assets/logos/linkedin.jpg")
    github_logo = get_base64_image("assets/logos/github.jpg")
    gmail_logo = get_base64_image("assets/logos/gmail.jpg")
    whatsapp_logo = get_base64_image("assets/logos/whatsapp.jpg")

    gmail = "ddatnguyen97@gmail.com"
    whatsapp = "+84 342627824"

    with st.container():
        col1, col2 = st.columns([0.2, 0.8])
        
        with col1:
            st.markdown(
                f"""
                    <style>
                    .profile-img img {{
                        height: 400px;
                        width: auto;
                        border-radius: 15px;
                    }}
                    </style>

                    <div class="profile-img">
                        <img src="data:image/jpeg;base64,{profile_img}">
                    </div>
                """,
                unsafe_allow_html=True
            )
            st.divider()
            st.text("Connect with me:")
            with st.container(
                horizontal=True,
                horizontal_alignment="left"
            ):
                create_social_links([
                (
                    "https://www.linkedin.com/in/dat-nguyen-209938252",
                    linkedin_logo,
                    "LinkedIn"
                ),
                (
                    "https://github.com/ddatnguyen97",
                    github_logo,
                    "GitHub"
                )
            ])
            with st.container(
                horizontal=True,
                horizontal_alignment="left"
            ):
                create_logo_holder(
                    logo=gmail_logo,
                )
                
                create_copy_box(
                    text=gmail,
                )
            
            with st.container(
                horizontal=True,
                horizontal_alignment="left"
            ):
                create_logo_holder(
                    logo=whatsapp_logo,
                )

                create_copy_box(
                    text=whatsapp,
                )
            
            create_spacer(2)
            with st.container():
                if st.download_button(
                    "Download My Resume",
                    data=open("assets/resume/Nguyen Hoang Quoc Dat Resume.pdf", "rb").read(),
                    file_name="Nguyen_Hoang_Quoc_Dat_Resume.pdf",
                ):
                    track_event(
                        "cv_download",
                        {"source": "about_me"}
                    )

        with col2:
            st.markdown(
                f"""
                <style>
                .job-title {{
                    color: #2bb179;
                }}
                </style>

                <div class="job-title">
                    <h2>
                        Hi, I'm Dat Nguyen
                    </h2>
                </div>
            """,
                unsafe_allow_html=True
            )
            with st.container():
                st.write(
                """
                    With a background in Management Information Systems (MIS), I focus on analytics engineering and data visualization. I work with SQL and Python to build reliable data pipelines, model analytical datasets, and deliver insights through dashboards and analytics applications. In parallel, I am developing foundational machine learning skills to apply predictive models to real-world analytics problems.
                """
                )

            with st.container():
                st.subheader(
                    "Education",
                    divider="green"
                )

                st.markdown(
                    """
                    #### 2020 – 2024&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;Hoa Sen University, Ho Chi Minh City, Vietnam
                    
                    - Bachelor of Management Information Systems (MIS) 
                    
                    - GPA: 3.27/4.0 - Good
                    """
                )

            with st.container():
                st.subheader(
                    "Skills",
                    divider="green"
                )
                with st.container():
                    col1, col2, col3 = st.columns(3)
                    
                    programing_languages = [
                        "Python",
                        "SQL"
                    ]

                    with col1:
                        st.write("Programming Languages")
                        with st.container(
                            horizontal=True
                        ):
                            for v in programing_languages:
                                st.badge(
                                    v,
                                    color="green"
                                )
                    
                    databases = [
                        "PostgreSQL",
                        "Google BigQuery"
                    ]

                    with col2:
                        st.write("Data Management & Modeling")
                        with st.container(
                            horizontal=True
                        ):
                            for v in databases:
                                st.badge(
                                    v,
                                    color="yellow"
                                )
                            
                    visualization_tools = [
                        "Microsoft Power BI",
                        "Google Looker Studio",
                        "Tableau",
                        "Superset",
                        "Streamlit"
                    ]

                    with col3:
                        st.write("Data Visualization & Reporting")
                        with st.container(
                            horizontal=True
                        ):
                            for v in visualization_tools:
                                st.badge(
                                    v,
                                    color="blue"
                                )

            with st.container():
                col1, col2, col3 = st.columns(3)
                
                data_analysis_skills = [
                    "Pandas",
                    "Exploratory Data Analysis (EDA)",
                    "Matplotlib",
                    "Seaborn",
                ]

                with col1:
                    st.write("Data Analysis")
                    with st.container(
                        horizontal=True
                    ):
                        for v in data_analysis_skills:
                                st.badge(
                                    v,
                                    color="red"
                                )
                
                data_engineering_skills = [
                    "ETL/ELT",
                    "Data Warehousing",
                ]

                with col2:
                    st.write("Analytics Engineering")
                    with st.container(
                        horizontal=True
                    ):
                        for v in data_engineering_skills:
                            st.badge(
                                v,
                                color="violet"
                            )

                machine_learning_skills = [
                    "Predictive Modeling (Basics)",
                    "Time Series Forecasting",
                    "Natural Language Processing (Basics)",
                ]

                with col3:
                    st.write("Machine Learning (Foundational)")
                    with st.container(
                        horizontal=True
                    ):
                        for v in machine_learning_skills:
                            st.badge(
                                v,
                                color="orange"
                            )
    
if __name__ == "__main__":
    create_about_me_page()