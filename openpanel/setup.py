import streamlit.components.v1 as components

def load_openpanel(client_id):
    components.html(
        f"""
        <script>
        window.op = window.op || function () {{
            var n = [];
            return new Proxy(function () {{
                arguments.length && n.push([].slice.call(arguments))
            }}, {{
                get: function (t, r) {{
                    return r === "q" ? n : function () {{
                        n.push([r].concat([].slice.call(arguments)))
                    }}
                }},
                has: function (t, r) {{
                    return r === "q"
                }}
            }})
        }}();

        window.op('init', {{
            clientId: "{client_id}",
            trackScreenViews: true,
            trackOutgoingLinks: true,
            trackAttributes: true,
        }});
        </script>

        <script src="https://openpanel.dev/op1.js" defer async></script>
        """,
        height=0
    )

