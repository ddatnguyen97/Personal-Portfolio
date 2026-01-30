import streamlit.components.v1 as components
import streamlit as st

def load_openpanel(client_id):
    components.html(
        f"""
        <script>
          (function() {{
            if (window.__openpanel_loaded__) return;
            window.__openpanel_loaded__ = true;

            window.op = window.op || function() {{
              (window.op.q = window.op.q || []).push(arguments);
            }};

            window.op('init', {{
              clientId: '{client_id}',
              trackScreenViews: false,
              trackOutgoingLinks: false,
              trackAttributes: true
            }});

            var s = document.createElement('script');
            s.src = 'https://openpanel.dev/op1.js';
            s.async = false;
            document.head.appendChild(s);
          }})();
        </script>
        """,
        height=0,
    )