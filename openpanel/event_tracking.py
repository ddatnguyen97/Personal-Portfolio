import json
import streamlit.components.v1 as components

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
