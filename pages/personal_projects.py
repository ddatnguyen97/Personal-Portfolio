import streamlit as st
from config import set_config
from utils import create_project_card
from openpanel.event_tracking import track_page
from openpanel.setup import load_openpanel

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
        vbp_content = """
            <ul>
                <li>Built an end-to-end analytics system for an online bookstore by extracting book metadata from the Google Books API and storing it in a structured PostgreSQL database</li>
                <li>Designed analytical data models and performed data cleaning and transformation using SQL and Python to support reporting use cases</li>
                <li>Developed an interactive Streamlit dashboard to analyze sales performance, customer behavior, and product trends, enabling data-driven insights for business decision-making</li>
            </ul>
        """
        vbp_tools = "PostgreSQL, SQL, Python, Streamlit"
        vbp_link = "https://github.com/ddatnguyen97/Virtual_Online_Book_Store"

        create_project_card(
                project_link=vbp_link,
                content=vbp_content,
                title=vbp_title,
                tools=vbp_tools,
                event_name=event_name,
                project_name="Virtual Online Bookstore Project"
            )

        wrp_title = "Weather Report Project"
        wrp_content = """
            <ul>
                <li>Designed and deployed a fully automated data pipeline to collect, process, and analyze hourly weather data from the Open-Meteo API</li>
                <li>Built ETL workflows using Python and SQL to clean and load data into Google BigQuery, with scheduling handled via GitHub Actions and cron jobs</li>
                <li>Developed an interactive real-time analytics dashboard using Dash and Plotly with direct BigQuery integrations</li>
                <li>Implemented Google Tag Manager and GA4 to track user interactions, storing event data in BigQuery and visualizing insights through dynamic Looker Studio reports</li>
            </ul>
        """
        wrp_tools = "BigQuery, SQL, Python, Dash, Plotly, Looker Studio, GA4, GTM"
        wrp_link = "https://github.com/ddatnguyen97/Weather-Dashboard"

        create_project_card(
                project_link=wrp_link,
                content=wrp_content,
                title=wrp_title,
                tools=wrp_tools,
                event_name=event_name,
                project_name="Weather Report Project"
            )

        ubp_title = "GA4 User Behavior and Demographics Analytics"
        ubp_content = """
            <ul>
                <li>Performed user behavior and demographic analysis using GA4 event data, with BigQuery serving as the central data warehouse</li>
                <li>Conducted Exploratory Data Analysis (EDA) in Python to identify usage patterns, engagement trends, and behavioral segments</li>
                <li>Developed custom SQL queries to define key metrics such as active users, new users, funnel stages, and weekly cohort retention</li>
                <li>Built interactive Looker Studio dashboards to visualize engagement across devices, operating systems, geographic regions, and interest categories, supporting data-driven product and marketing insights</li>
            </ul>
        """
        ubp_tools = "BigQuery, SQL (Custom Queries), Python (Google Colab), Looker Studio"
        ubp_link = "https://github.com/ddatnguyen97/User-Behavior-And-Demographics-Analytics"

        create_project_card(
            project_link=ubp_link,
            content=ubp_content,
            title=ubp_title,
            tools=ubp_tools,
            event_name=event_name,
            project_name="GA4 User Behavior and Demographics Analytics Project"
        )    

if __name__ == "__main__":
    create_projects_page()
