import streamlit.components.v1 as components
import streamlit as st

def load_openpanel(client_id):
    st.markdown(
        f"""
        <script>
          window.op = window.op || [];
          window.op.push(['init', {{
            clientId: '{client_id}',
            trackScreenViews: true,
            trackOutgoingLinks: true,
            trackAttributes: true,
          }}]);
        </script>
        <script src="https://openpanel.dev/op1.js" async></script>
        """,
        unsafe_allow_html=True
    )