# Färger per åldersgrupp (BoKoll-paletten i gradient)
FARGER = {
    "0-9":   "#003F47",  # Mörk teal
    "10-19": "#41564D",  # Mörkgrön
    "20-29": "#738168",  # Salviegrön
    "30-39": "#6F8E90",  # Dämpad teal
    "40-49": "#A2C1C6",  # Ljusblå
    "50-59": "#D8BD86",  # Sandbeige
    "60-69": "#B59775",  # Brun-beige
    "70-79": "#E39D4D",  # Orange
    "80+":   "#7A4F2A",  # Mörk brun
}

# Ordning på åldersgrupperna i diagrammet
ORDNING = ["0-9", "10-19", "20-29", "30-39", "40-49",
           "50-59", "60-69", "70-79", "80+"]


def styla_bar_befolkning(fig):
    # Stil på själva staplarna med värden ovanför
    fig.update_traces(
        marker=dict(line=dict(color="white", width=2)),
        texttemplate="%{y:.1s}",
        textposition="outside",
        textfont=dict(size=12, color="#333"),
    )

    # Layout för hela diagrammet
    fig.update_layout(
        showlegend=False,
        xaxis=dict(
            title="Åldersgrupper",
            tickfont=dict(size=12),
            showgrid=False,
        ),
        yaxis=dict(
            title="Antal",
            tickfont=dict(size=11),
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)",
            tickformat="~s",
        ),
        margin=dict(t=20, b=40, l=40, r=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        bargap=0.3,
    )

    return fig