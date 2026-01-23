import base64
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def create_link_button(link=None, logo=None):
    st.markdown(
        f"""
        <style>
        .social-icon {{
            width: 36px;
            height: 36px;
            cursor: pointer;
        }}
        </style>

        <a href="{link}" target="_blank">
            <img src="data:image/png;base64,{logo}"
                 class="social-icon">
        </a>
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
    keywords = {
        # Core foundations
        "SQL": 90,
        "Python": 90,
        "Data Analytics": 100,
        "Data Engineering": 90,
        "Analytics Engineering": 90,

        # Data pipeline & processing
        "ETL": 85,
        "ELT": 80,
        "Data Pipelines": 85,
        "Data Modeling": 80,
        "Data Transformation": 75,
        "Data Quality": 70,
        "Data Validation": 65,
        "Data Cleaning": 70,
        "Data Preprocessing": 65,

        # Analytics & BI
        "Business Intelligence": 75,
        "KPI": 65,
        "Metrics": 60,
        "Dashboards": 65,
        "Reporting": 60,
        "Ad-hoc Analysis": 55,
        "Exploratory Data Analysis": 55,
        "EDA": 50,
        "Insights": 60,
        "Decision Support": 55,

        # Databases & modeling
        "PostgreSQL": 70,
        "MySQL": 65,
        "BigQuery": 82,
        "Data Warehouse": 80,
        "Data Mart": 65,
        "Fact Tables": 60,
        "Dimension Tables": 60,
        "Star Schema": 65,

        # Engineering tools
        "Airflow": 64,
        "dbt": 62,
        "PySpark": 52,
        "Docker": 50,
        "Git": 50,

        # Visualization
        "Power BI": 86,
        "Looker Studio": 85,
        "Tableau": 65,
        "Apache Superset": 60,
        "Streamlit": 78,

        # Cloud & integration
        "Google Cloud Platform": 70,
        "GCP": 65,
        "Cloud Storage": 60,
        "APIs": 65,

        # Machine learning (supporting role)
        "Feature Engineering": 60,
        "Data Preparation": 60,
        "Model Evaluation": 55,
        "Prediction": 50,
        "Time Series": 55
    }
    
    size = 500
    x, y = np.ogrid[:size, :size]
    center = (size // 2, size // 2)
    radius = size // 2 - 10

    mask = (x - center[0])**2 + (y - center[1])**2 > radius**2
    mask = 255 * mask.astype(int)

    wordcloud = WordCloud(
        width=150,
        height=150,
        mask=mask,
        background_color="#0E1117",
        colormap="rainbow",
        min_font_size=5,
        collocations=False
    ).generate_from_frequencies(keywords)

    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_visible(False)
    ax.set_facecolor("none")

    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")

    plt.tight_layout(pad=0)

    st.pyplot(fig)