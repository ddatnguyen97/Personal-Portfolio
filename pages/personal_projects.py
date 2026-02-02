import streamlit as st
from config import set_config
from utils import create_project_card
from openpanel.event_tracking import track_page

import os
from dotenv import load_dotenv

load_dotenv()

def create_projects_page():
    if "tracked_projects" not in st.session_state:
        track_page("Personal Projects")
        st.session_state.tracked_projects = True

    page_title = "Personal Projects"
    set_config(
        title=page_title,
    )

    event_name = "project_view"

    st.header(
        "Personal Projects",
        divider="green"
    )
    with st.container():
        vbp_title = "Virtual Online Bookstore Project"
        vbp_content = (
            "• Built an end-to-end analytics system for an online bookstore by extracting book metadata from the Google Books API and storing it in PostgreSQL\n"
            "• Designed analytical data models and performed data cleaning and transformations using SQL and Python to support reporting use cases\n"
            "• Developed an interactive Streamlit dashboard to analyze sales performance, customer behavior, and product trends, enabling data-driven business insights"
        )
        vbp_tools = "PostgreSQL, SQL, Python, Streamlit"
        vbp_link = "https://github.com/ddatnguyen97/Virtual_Online_Book_Store"

        create_project_card(
                project_link=vbp_link,
                description=vbp_content, 
                tools=vbp_tools,
                title=vbp_title,
            )

        wrp_title = "Weather Report Project"
        wrp_content = (
            "• Designed and deployed a fully automated data pipeline to collect, process, and analyze hourly weather data from the Open-Meteo API\n"
            "• Built ETL workflows using Python and SQL to clean and load data into Google BigQuery, with scheduling handled via GitHub Actions and cron jobs\n"
            "• Developed an interactive real-time analytics dashboard using Dash and Plotly with direct BigQuery integrations\n"
            "• Implemented Google Tag Manager and GA4 to track user interactions, storing event data in BigQuery and visualizing insights through dynamic Looker Studio reports"
        )

        wrp_tools = "BigQuery, SQL, Python, Dash, Plotly, Looker Studio, GA4, GTM"
        wrp_link = "https://github.com/ddatnguyen97/Weather-Dashboard"

        create_project_card(
                project_link=wrp_link,
                description=wrp_content,
                tools=wrp_tools,
                title=wrp_title,
            )

        ubp_title = "GA4 User Behavior and Demographics Analytics"
        ubp_content = (
            "• Analyzed user behavior and demographics using GA4 event data with BigQuery as the central data warehouse\n"
            "• Performed exploratory data analysis (EDA) in Python to uncover usage patterns, engagement trends, and behavioral segments\n"
            "• Wrote custom SQL queries to define key metrics including active users, new users, funnel stages, and weekly cohort retention\n"
            "• Built interactive Looker Studio dashboards visualizing engagement by device, OS, geography, and interest categories to support data-driven product and marketing decisions"
        )
        ubp_tools = "BigQuery, SQL (Custom Queries), Python (Google Colab), Looker Studio"
        ubp_link = "https://github.com/ddatnguyen97/User-Behavior-And-Demographics-Analytics"

        create_project_card(
            project_link=ubp_link,
            description=ubp_content,
            tools= ubp_tools,
            title=ubp_title,
        )

if __name__ == "__main__":
    create_projects_page()
