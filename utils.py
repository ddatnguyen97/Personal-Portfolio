import base64
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random

def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# def create_link_button(link=None, logo=None, event_name=None, social_name=None):
#     event_name = event_name or "click_external_link"

#     st.markdown(
#         f"""
#         <style>
#         .social-icon {{
#             width: 36px;
#             height: 36px;
#             cursor: pointer;
#         }}
#         </style>

#         <a href="{link}" target="_blank"
#            onclick="event.preventDefault(); if (window.op) {{ window.op('track', '{event_name}', {{ social_name: '{social_name}', url: '{link}' }}); }} setTimeout(function() {{ window.open('{link}', '_blank'); }}, 150);">
#             <img src="data:image/png;base64,{logo}" class="social-icon">
#         </a>
#         """,
#         unsafe_allow_html=True
#     )

def create_link_button(link, logo, social_name):
    st.markdown(
        f"""
        <a href="{link}"
           onclick="event.preventDefault(); trackAndGo(
               'click_external_link',
               {{ social_name: '{social_name}' }},
               '{link}'
           );">
            <img src="data:image/png;base64,{logo}" class="social-icon">
        </a>
        """,
        unsafe_allow_html=True
    )

def create_logo_holder(logo):
    st.markdown(
        f"""
        <style>
        .social-icon {{
            width: 36px;
            height: 36px;
            cursor: pointer;
        }}
        </style>

        <img src="data:image/png;base64,{logo}"
                class="social-icon">
        </a>
        """,
        unsafe_allow_html=True
    )

def create_copy_box(text):
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
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )

def create_spacer(height=None):
    st.markdown(f"<div style='height:{height}px'></div>", unsafe_allow_html=True)

def create_vertical_divider(color="rgba(255,255,255,0.3)", height="auto"):
    st.markdown(
        f"""
        <div style="border-left:2px solid {color}; height:{height};"></div>
        """,
        unsafe_allow_html=True
    )

def create_wordcloud():
    keywords = [
        # Core foundations
        "SQL",
        "Python",
        "Data Analytics",
        "Data Engineering",
        "Analytics Engineering",

        # Data pipeline & processing
        "ETL",
        "ELT",
        "Data Pipelines",
        "Data Modeling",
        "Data Transformation",
        "Data Quality",
        "Data Validation",
        "Data Cleaning",
        "Data Preprocessing",

        # Analytics & BI
        "Business Intelligence",
        "KPI",
        "Metrics",
        "Dashboards",
        "Reporting",
        "Ad-hoc Analysis",
        "Exploratory Data Analysis",
        "Insights",
        "Decision Support",

        # Databases & modeling
        "PostgreSQL",
        "MySQL",
        "BigQuery",
        "Data Warehouse",
        "Data Mart",
        "Fact Tables",
        "Dimension Tables",
        "Star Schema",
        "Snowflake Schema",

        # Engineering tools
        "Airflow",
        "dbt",
        "PySpark",
        "Docker",
        "Git",

        # Visualization
        "Power BI",
        "Looker Studio",
        "Tableau",
        "Apache Superset",
        "Streamlit",

        # Cloud & integration
        "Google Cloud Platform",
        "Cloud Storage",
        "APIs",

        # Machine learning (supporting role)
        "Feature Engineering",
        "Data Preparation",
        "Model Evaluation",
        "Prediction",
        "Time Series"
    ]

    freqs = dict(
        zip(
            keywords,
            [random.randint(40, 100) for _ in keywords]
        )
    )

    size = 1000 
    x, y = np.ogrid[:size, :size]
    center = size // 2
    radius = size // 2

    mask = (x - center)**2 + (y - center)**2 > radius**2
    mask = mask.astype(np.uint8) * 255

    wordcloud = WordCloud(
        mask=mask,
        background_color="#0E1117",
        colormap="rainbow",
        min_font_size=5,
        collocations=False
    ).generate_from_frequencies(freqs)

    fig, ax = plt.subplots(figsize=(3, 3))
    fig.patch.set_visible(False)
    ax.set_facecolor("none")

    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")

    plt.tight_layout(pad=0)

    st.pyplot(fig)

def create_project_card(project_link, title, tools, content=None, event_name=None, project_name=None):
    event_name = event_name or "view_project"

    st.markdown(
        f"""
        <style>
        .project-card {{
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
            transition: 0.2s;
            cursor: pointer;
            background-color: #141414;
        }}

        .project-card:hover {{
            box-shadow: 0 4px 14px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }}

        .project-title {{
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 6px;
            color: #00a99d;
        }}

        .project-desc {{
            color: #E4E4E5;
            margin-bottom: 8px;
        }}

        .project-tools {{
            font-size: 15px;
            color: #1E73CE;
        }}
        </style>

        <a href="{project_link}" 
                    target="_blank" 
                    style="text-decoration:none; color:inherit;"
                    onclick="event.preventDefault();
           trackAndGo(
                '{event_name}',
                {{ project_name: '{project_name}', url: '{project_link}' }},
                '{project_link}'
            );">
            <div class="project-card">
                <div class="project-title">{title}</div>
                <div class="project-desc">{content}</div>
                <div class="project-tools">🛠 {tools}</div>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
