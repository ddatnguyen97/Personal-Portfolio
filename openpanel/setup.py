import streamlit.components.v1 as components
import streamlit as st

def load_openpanel(client_id):
    st.markdown(
        f"""
        <script>
          (function() {{
            window.op = window.op || function() {{
              (window.op.q = window.op.q || []).push(arguments);
            }};

            window.op('init', {{
              clientId: '{client_id}',
              trackScreenViews: false,
              trackOutgoingLinks: false,
              trackAttributes: true
            }});
          }})();
        </script>
        <script src="https://openpanel.dev/op1.js" async></script>
        """,
        unsafe_allow_html=True
    )