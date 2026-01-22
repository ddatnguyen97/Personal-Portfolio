import base64
import streamlit as st

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

def spacer(height=None):
    st.markdown(f"<div style='height:{height}px'></div>", unsafe_allow_html=True)
