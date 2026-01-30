import streamlit as st
from config import set_config
from openpanel.event_tracking import track_page
from openpanel.setup import load_openpanel

import os
from dotenv import load_dotenv

load_dotenv()

def create_experience_page():
    if "tracked_about" not in st.session_state:
        track_page("Experience")
        st.session_state.tracked_about = True

    page_titile = "Experience"
    set_config(
        title=page_titile,
    )

    st.header(
        "Experience",
        divider="green"
    )

    vita_dairy_tech_stack = {
            "Python": "green",
            "Pandas": "red",
            "Salesforce CRM": "yellow",
            "Google Looker Studio": "blue",
        }
    with st.container():
        col1, col2 = st.columns([0.3, 0.7])

        with col1:
            st.markdown(
                f"""
                <style>
                .job-title {{
                    color: #2bb179;
                }}
                </style>

                <div class="job-title">
                    <h3>
                        CRM - Data Analyst
                    </h3>
                </div>
            """,
                unsafe_allow_html=True
            )
            st.markdown(
                """
                ##### :blue[VitaDairy Joint Stock Company]

                _Jul, 2025 - Nov, 2025 | Ho Chi Minh City, Vietnam_            
            """
            )
            st.markdown(
                    "Tech stacks:"
                )
            with st.container(
                horizontal=True
            ):
                for tech, color in vita_dairy_tech_stack.items():
                    st.badge(
                        tech,
                        color=color
                    )

        with col2:
            st.markdown(
                "##### Responsibilities:"
            )
            st.markdown(
                """
                - Utilized Python to integrate and process data from multiple sources (HRIS, Salesforce CRM, Loyalty App, etc) to build performance evaluation reports for Promotion Girls (PGs) based on Sales team requirements
                - Used Python to process and analyze data from Salesforce CRM and Google Looker to create brand performance reports, enabling Marketing teams to monitor brand effectiveness and campaign performance
                - Built and maintained a centralized Salesforce CRM data source optimized for reporting, analytical, and operational purposes
                - Participated in a customer authentication project using voice OTP, then analyzed customers' point accumulation behavior through the loyalty app, and developed reports to evaluate the performance of promotion girls
                - Performed ad-hoc analyzes as requested by each department
                """
            )

            st.markdown(
                "##### Results:"
            )
            st.markdown(
                """
                - Reduced data preprocessing time by automating data integration and transformation workflows using Python
                - Improved data quality and consistency by implementing standardized data preprocessing pipelines across multiple data sources
                - Enabled Sales and Marketing teams to make data-driven decisions by delivering timely and reliable performance reports for Promotion Girls and brand campaigns
                """
            )
            
    st.divider()

    vietdata_tech_stack = {
        "SQL": "green",
        "Google Analytics": "violet",
        "Google Tag Manager": "violet",
        "Google BigQuery": "yellow",
        "Google Looker Studio": "blue"
    }
    with st.container():
        col1, col2 = st.columns([0.3, 0.7])

        with col1:
            st.markdown(
                f"""
                <style>
                .job-title {{
                    color: #2bb179;
                }}
                </style>

                <div class="job-title">
                    <h3>
                        Data Analyst
                    </h3>
                </div>
            """,
                unsafe_allow_html=True
            )
            st.markdown(
                """
                ##### :blue[VietData.AI CO, LTD]

                _Jan, 2025 - May, 2025 | Ho Chi Minh City, Vietnam_            
            """
            )
            st.markdown(
                "Tech stacks:"
            )
            with st.container(
                horizontal=True
            ):
                for tech, color in vietdata_tech_stack.items():
                    st.badge(
                        tech,
                        color=color
                    )

        with col2:
            st.markdown(
                "##### Responsibilities:"
            )
            st.markdown(
                """
                - Focused on cloud-based analytics and AI-enabled data solutions to support digital transformation initiatives
                - Audited website analytics setups to identify and resolve missing, incorrect, or inconsistent event parameters
                - Implemented Google Analytics 4 (GA4) and Google Tag Manager (GTM) to ensure accurate and scalable event tracking across websites
                - Validated tracking implementations using GTM Preview Mode and GA4 DebugView to ensure data accuracy and completeness
                - Standardized dataLayer structure and event schemas in alignment with GA4 best practices to support reliable downstream analytics
                - Authored detailed technical documentation and implementation guides for developers, improving collaboration and consistency in data tracking
                - Integrated GA4 with Google BigQuery to access raw event-level data and performed SQL-based analysis to generate actionable insights
                - Utilized GA4, BigQuery, and Looker Studio to deliver dashboards and analytical reports that supported business and marketing decisions
                """
            )

            st.markdown(
                "##### Results:"
            )
            st.markdown(
                """
                - Improved the accuracy and reliability of digital analytics data by standardizing event tracking and validating implementations across web properties
                - Reduced data discrepancies and tracking errors through systematic auditing and debugging of GA4 and GTM configurations
                - Enhanced collaboration between analytics and development teams through clear documentation and standardized dataLayer guidelines
                """
            )
            
    st.divider()

    onemedic_tech_stack = {
        "SQL": "green",
        "Python": "green",
        "Pandas": "red",
        "Data Warehousing": "violet",
        "Airflow": "violet",
        "PostgreSQL": "yellow",
        "Superset": "blue"
    }
    with st.container():
        col1, col2 = st.columns([0.3, 0.7])

        with col1:
            st.markdown(
                f"""
                <style>
                .job-title {{
                    color: #2bb179;
                }}
                </style>

                <div class="job-title">
                    <h3>
                        Data Analytics Engineer Intern
                    </h3>
                </div>
            """,
                unsafe_allow_html=True
            )
            st.markdown(
                """
                ##### :blue[OneMedic Joint Stock Company]

                _Sep, 2024 - Dec, 2024 | Ho Chi Minh City, Vietnam_            
            """
            )
            st.markdown(
                "Tech stacks:"
            )
            with st.container(
                horizontal=True
            ):
                for tech, color in onemedic_tech_stack.items():
                    st.badge(
                        tech,
                        color=color
                    )

        with col2:
            st.markdown(
                "##### Responsibilities:"
            )
            st.markdown(
                """
                - Focused on integrating AI-driven X-ray diagnostic reports for pulmonary diseases and performing in-depth analysis of medical data
                - Designed and implemented a scalable data warehouse for the Medic BI system to enhance analytics and reporting
                - Optimized data querying using SQL and developed advanced data preprocessing workflows with Python preprocessing workflows with Python
                - Built and automated a robust ETL pipeline using Airflow, ensuring timely and accurate data integration and accurate data integration
                - Developed and maintained interactive dashboards in Superset to visualize key medical examination and treatment metrics key medical examination and treatment metrics
                """
            )

            st.markdown(
                "##### Results:"
            )
            st.markdown(
                """
                - Improved data availability and consistency by automating end-to-end ETL pipelines with Airflow, ensuring timely and accurate integration of medical and diagnostic data
                - Reduced query execution time and improved analytical performance through SQL query optimization and efficient data modeling
                - Supported data-driven evaluation of pulmonary diagnostic workflows by providing clean, structured, and analytics-ready datasets for BI reporting
                """
            )

if __name__ == "__main__":
    create_experience_page()
