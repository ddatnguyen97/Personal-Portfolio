import json
import streamlit.components.v1 as components
import streamlit as st


def load_openpanel(client_id: str):
    """Load the OpenPanel snippet into the Streamlit app.

    Args:
        client_id: OpenPanel client ID (non-empty string).
    """
    if not client_id or not isinstance(client_id, str):
        raise ValueError("client_id must be a non-empty string")

    # Use a plain string (not an f-string) to avoid having to escape JS braces.
    html = """
    <script>
        window.op = window.op || function(){ var n = []; return new Proxy(function(){ arguments.length && n.push([].slice.call(arguments)) }, { get: function(t, r) { return "q" === r ? n : function(){ n.push([r].concat([].slice.call(arguments))) } } , has: function(t, r) { return "q" === r } }) }();
        window.op('init', {
            clientId: 'YOUR_CLIENT_ID',
            trackScreenViews: true,
            trackOutgoingLinks: true,
            trackAttributes: true,
        });
    </script>
    <script src="https://openpanel.dev/op1.js" defer async></script>
    """

    # Safely inject the client_id (json.dumps ensures proper quoting/escaping)
    html = html.replace('YOUR_CLIENT_ID', json.dumps(client_id))

    components.html(html, height=0)
