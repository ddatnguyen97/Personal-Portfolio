import base64
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random
from streamlit_card import card

def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# def create_link_button(link, logo, social_name):
#     components.html(
#         f"""
#         <a href="{link}"
#            target="_blank"
#            onclick="
#              window.op('track', 'external_link_click', {{
#                social_name: '{social_name}',
#                url: '{link}'
#              }});
#            ">
#           <img src="data:image/png;base64,{logo}" width="36" />
#         </a>
#         """,
#         height=50
#     )

def create_social_links(links):
    icons_html = ""

    for link, logo, social_name in links:
        icons_html += f"""
        <a href="{link}" target="_blank"
           style="margin-right:12px; display:inline-block;"
           onclick="
             if (window.op) {{
               window.op('track', 'external_link_click', {{
                 social_name: '{social_name}',
                 url: '{link}'
               }});
             }}
           ">
          <img src="data:image/png;base64,{logo}" width="36" />
        </a>
        """

    components.html(
        f"""
        <div style="display:flex; align-items:center;">
            {icons_html}
        </div>
        """,
        height=50
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

def create_project_card(project_link, title, description, tools):
    card(
        title=title,
        text=[
            description,
            f"🛠 Tools: {tools}"
        ],
        url=project_link,
        styles={
            "card": {
                "width": "100%",
                "background-color": "#141414",
                "border": "1px solid rgba(255,255,255,0.15)",
                "border-radius": "16px",
                "padding": "20px",
                "box-shadow": "0 8px 24px rgba(0,0,0,0.35)",
                "margin": "0px",
            },
            "title": {
                "color": "#1E73CE",
                "font-size": "24px",
                "font-weight": "600",
                "margin-bottom": "12px",
                "text-align": "left",
            },
            "text": {
                "color": "#E6E6E6",
                "font-size": "16px",
                "line-height": "1.6",
                "white-space": "pre-line",
                "text-align": "left",
            },
        }
    )

