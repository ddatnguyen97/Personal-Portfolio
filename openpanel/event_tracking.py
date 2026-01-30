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
          (function() {{
            window.op = window.op || function() {{
              (window.op.q = window.op.q || []).push(arguments);
            }};

            window.op('init', {{
              clientId: '{os.getenv("OPENPANEL_CLIENT_ID")}'
            }});

            window.op('track', '{event_name}', {props});
          }})();
        </script>
        <script src="https://openpanel.dev/op1.js" async></script>
        """,
        height=0
    )

def track_page(page_name):
    components.html(
        f"""
        <script>
          (function() {{
            window.op = window.op || function() {{
              (window.op.q = window.op.q || []).push(arguments);
            }};

            window.op('init', {{
              clientId: '{os.getenv("OPENPANEL_CLIENT_ID")}'
            }});

            window.op('track', 'page_view', {{
              page: '{page_name}'
            }});
          }})();
        </script>
        <script src="https://openpanel.dev/op1.js" async></script>
        """,
        height=0
    )
