import json
import streamlit.components.v1 as components

def track_event(event_name, properties=None):
    props = json.dumps(properties or {})

    components.html(
        f"""
        <script>
        if (window.trackAndGo) {{
            window.trackAndGo(
                '{event_name}',
                {props}
            );
        }}
        </script>
        """,
        height=0
    )

def track_page(page_name):
    components.html(
        f"""
        <script>
        if (window.trackAndGo) {{
            window.trackAndGo(
                'page_view',
                {{ page: '{page_name}' }}
            );
        }}
        </script>
        """,
        height=0
    )
