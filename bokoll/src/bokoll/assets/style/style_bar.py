# Färger per upplåtelseform (BoKoll-paletten)
FARGER = {
    "Bostadsrätt": "#738168",   # Salviegrön
    "Hyresrätt":   "#B59775",   # Beige
    "Äganderätt":  "#E39D4D",   # Orange
}


def styla_bar(fig):
    # Stil på själva staplarna (vita kanter, värden ovanför)
    fig.update_traces(
        marker=dict(line=dict(color="white", width=2)),
        texttemplate="%{y:,.0f}",
        textposition="outside",
        textfont=dict(size=12),
    )

    # Layout för hela diagrammet
    fig.update_layout(
        showlegend=False,
        xaxis=dict(
            title="",
            tickangle=-30,
            tickfont=dict(size=12),
        ),
        yaxis=dict(
            title="Antal hushåll",
            tickfont=dict(size=11),
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)",
            tickformat=",",
        ),
        margin=dict(t=20, b=40, l=40, r=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        bargap=0.4,
    )

    return fig