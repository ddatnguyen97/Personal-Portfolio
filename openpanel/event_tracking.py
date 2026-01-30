import json
import streamlit.components.v1 as components
import os
from dotenv import load_dotenv

load_dotenv()

def track_event(event_name, properties=None):
    props = json.dumps(properties or {})
    components.html(
        f"""
        <script>
          if (window.op) {{
            window.op('track', '{event_name}', {props});
          }}
        </script>
        """,
        height=0
    )

def track_page(page_name):
    components.html(
        f"""
        <script>
          if (window.op) {{
            window.op('track', 'page_view', {{
              page: '{page_name}'
            }});
          }}
        </script>
        """,
        height=0
    )


