import streamlit as st
from config import set_config
from utils import get_base64_image, create_link_button, spacer

def create_about_me_page():
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
                create_link_button(
                    "https://www.linkedin.com/in/dat-nguyen-209938252",
                    linkedin_logo
                )

                create_link_button(
                    "https://github.com/ddatnguyen97",
                    github_logo
                )
            
            spacer(2)
            with st.container(
                horizontal=True,
                horizontal_alignment="left"
            ):
                create_link_button(
                    logo=gmail_logo,
                )
                
                st.markdown(
                    f"""
                    <style>
                    .copy-box {{
                        padding: 8px 12px;
                        background-color: #1e1e1e;
                        border-radius: 6px;
                        cursor: pointer;
                        user-select: all;
                    }}
                    </style>

                    <div class="copy-box">
                        {gmail}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            spacer(2)
            with st.container(
                horizontal=True,
                horizontal_alignment="left"
            ):
                create_link_button(
                    logo=whatsapp_logo,
                )

                st.markdown(
                    f"""
                    <style>
                    .copy-box {{
                        padding: 8px 12px;
                        background-color: #1e1e1e;
                        border-radius: 6px;
                        cursor: pointer;
                        user-select: all;
                    }}
                    </style>

                    <div class="copy-box">
                        {whatsapp}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            spacer(2)
            with st.container():
                st.download_button(
                    "Download My Resume",
                    data=open("assets/resume/Nguyen_Hoang_Quoc_Dat_Resume.pdf", "rb").read(),
                    file_name="Nguyen_Hoang_Quoc_Dat_Resume.pdf",
                    type="primary"
                )

        with col2:
            st.header("Hi, I'm Dat Nguyen")
            with st.container():
                st.write(
                """
                    I am a Data Analytics Engineer with a background in Management Information Systems (MIS), focused on analytics engineering and data visualization. I work with SQL and Python to build reliable data pipelines, model analytical datasets, and deliver insights through dashboards and analytics applications. In parallel, I am developing foundational machine learning skills to apply predictive models to real-world analytics problems.
                """
                )

            with st.container():
                st.subheader(
                    "Background",
                    divider="green"
                )

                st.markdown(
                    """
                    #### 2020 – 2024 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Hoa Sen University, Ho Chi Minh City, Vietnam
                    
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
                    
                    with col1:
                        st.write("Programming Languages")
                        with st.container(
                            horizontal=True
                        ):
                            st.badge(
                                "Python",
                                color="green"
                            )
                            st.badge(
                                "SQL",
                                color="green"
                            )
                    
                    with col2:
                        st.write("Data Management & Modeling")
                        with st.container(
                            horizontal=True
                        ):
                            st.badge(
                                "PostgreSQL",
                                color="yellow"
                            )
                            st.badge(
                                "Google BigQuery",
                                color="yellow"
                            )

                    with col3:
                        st.write("Data Visualization & Reporting")
                        with st.container(
                            horizontal=True
                        ):
                            st.badge(
                                "Microsoft Power BI",
                                color="blue"
                            )
                            st.badge(
                                "Google Looker Studio",
                                color="blue"
                            )
                            st.badge(
                                "Tableau",
                                color="blue"
                            )
                            st.badge(
                                "Superset",
                                color="blue"
                            )
                            st.badge(
                                "Streamlit",
                                color="blue"
                            )

            with st.container():
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write("Data Analysis")
                    with st.container(
                        horizontal=True
                    ):
                        st.badge(
                            "Pandas",
                            color="red"
                        )
                        st.badge(
                            "Exploratory Data Analysis (EDA)",
                            color="red"
                        )
                
                with col2:
                    st.write("Analytics Engineering")
                    with st.container(
                        horizontal=True
                    ):
                        st.badge(
                            "ETL/ELT",
                            color="violet"
                        )
                        st.badge(
                            "Data Warehousing",
                            color="violet"
                        )

                with col3:
                    st.write("Machine Learning (Foundational)")
                    with st.container(
                        horizontal=True
                    ):
                        st.badge(
                            "Predictive Modeling (Basics)",
                            color="orange"
                        )
                        st.badge(
                            "Time Series Forecasting",
                            color="orange"
                        )
                        st.badge(
                            "Natural Language Processing (Basics)",
                            color="orange"
                        )
    
if __name__ == "__main__":
    create_about_me_page()