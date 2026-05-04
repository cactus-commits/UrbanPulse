# # Färger per upplåtelseform (BoKoll-paletten)
# FARGER = {
#     "Bostadsrätt": "#738168",   # Salviegrön
#     "Hyresrätt":   "#B59775",   # Beige
#     "Äganderätt":  "#E39D4D",   # Orange
# }


# def styla_bar(fig):
#     # Stil på själva staplarna (vita kanter, värden ovanför)
#     fig.update_traces(
#         marker=dict(line=dict(color="white", width=2)),
#         texttemplate="%{y:,.0f}",
#         textposition="outside",
#         textfont=dict(size=12),
#     )

#     # Layout för hela diagrammet
#     fig.update_layout(
#         showlegend=False,
#         xaxis=dict(
#             title="",
#             tickangle=-30,
#             tickfont=dict(size=12),
#         ),
#         yaxis=dict(
#             title="Antal hushåll",
#             tickfont=dict(size=11),
#             showgrid=True,
#             gridcolor="rgba(0,0,0,0.05)",
#             tickformat=",",
#         ),
#         margin=dict(t=20, b=40, l=40, r=20),
#         paper_bgcolor="rgba(0,0,0,0)",
#         plot_bgcolor="rgba(0,0,0,0)",
#         bargap=0.4,
#     )

#     return fig

# style.py


import altair as alt

FARGER = {
    "Bostadsrätt": "#738168",
    "Hyresrätt":   "#B59775",
    "Äganderätt":  "#E39D4D",
}

def bygg_bar(df):
    base = alt.Chart(df).encode(
        x=alt.X("Upplåtelseform_Stor:N", sort="-y", title="",
                axis=alt.Axis(labelAngle=-30)),
        y=alt.Y("value:Q", title="Antal hushåll",
                axis=alt.Axis(format="~s")),
        color=alt.Color(
            "Upplåtelseform_Stor:N",
            scale=alt.Scale(domain=list(FARGER), range=list(FARGER.values())),
            legend=None,
        ),
    )

    bars   = base.mark_bar(stroke="white", strokeWidth=2, size=40)
    labels = base.mark_text(dy=-6, align="center", baseline="bottom").encode(
        text=alt.Text("value:Q", format=",.0f")
    )

    return (
        (bars + labels)
        .properties(height=350)
        .configure_view(strokeWidth=0)
        .configure_axis(gridOpacity=0.05)
    )