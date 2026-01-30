import streamlit.components.v1 as components
import streamlit as st

def load_openpanel(client_id):
    components.html(
    f"""
    <script>
      (function() {{
        window.op = window.op || function() {{
          (window.op.q = window.op.q || []).push(arguments);
        }};

        window.op('init', {{
          clientId: '{client_id}'
        }});

        window.op('track', 'page_view', {{
          page: 'Experience'
        }});
      }})();
    </script>
    <script src="https://openpanel.dev/op1.js" async></script>
    """,
    height=0
)
