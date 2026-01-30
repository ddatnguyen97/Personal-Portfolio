import streamlit.components.v1 as components
import streamlit as st

def load_openpanel(client_id):
    components.html(
        f"""
        <script>
          window.op = window.op || function () {{
            (op.q = op.q || []).push(arguments);
          }};

          window.op('init', {{
            clientId: "{client_id}",
            trackScreenViews: false,
            trackOutgoingLinks: false,
            trackAttributes: true,
          }});
        </script>

        <script src="https://openpanel.dev/op1.js" async></script>
        """,
        height=0,
    )