import streamlit.components.v1 as components

def load_openpanel(client_id):
    # components.html(
    #     f"""
    #     <script>
    #     window.op = window.op || function () {{
    #         var n = [];
    #         return new Proxy(function () {{
    #             arguments.length && n.push([].slice.call(arguments))
    #         }}, {{
    #             get: function (t, r) {{
    #                 return r === "q" ? n : function () {{
    #                     n.push([r].concat([].slice.call(arguments)))
    #                 }}
    #             }},
    #             has: function (t, r) {{
    #                 return r === "q"
    #             }}
    #         }})
    #     }}();

    #     window.op('init', {{
    #         clientId: "{client_id}",
    #         trackScreenViews: false,
    #         trackOutgoingLinks: false,
    #         trackAttributes: true,
    #     }});
    #     </script>

    #     <script src="https://openpanel.dev/op1.js" defer async></script>
    #     """,
    #     height=0
    # )
    components.html(
        f"""
        <script>
        /* ---- OpenPanel bootstrap (REQUIRED) ---- */
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
            trackScreenViews: false,   // you're manually controlling this
            trackOutgoingLinks: false, // important: disable auto, do manual
            trackAttributes: true,
        }});
        </script>

        <script src="https://openpanel.dev/op1.js" defer async></script>

        <script>
        /* ---- Safe event helper for Streamlit iframe ---- */
        (function () {{
            function trackAndGo(eventName, props, url) {{
                function tryTrack() {{
                    if (window.op && typeof window.op === 'function' && !window.op.q) {{
                        window.op('track', eventName, props || {{}});
                        if (url) {{
                            setTimeout(function () {{
                                window.open(url, '_blank');
                            }}, 200);
                        }}
                    }} else {{
                        setTimeout(tryTrack, 50);
                    }}
                }}
                tryTrack();
            }}
            window.trackAndGo = trackAndGo;
        }})();
        </script>
        """,
        height=0
    )

