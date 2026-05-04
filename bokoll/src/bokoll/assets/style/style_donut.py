# Färger för donut-diagrammet (BoKoll-paletten)
FARGER = {
    "Barn (0-19)":   "#6F8E90",  # Dämpad teal/blågrå
    "Unga (20-39)":  "#A2C1C6",  # Ljusblå
    "Vuxna (40-64)": "#D8BD86",  # Sandbeige
    "Äldre (65+)":   "#E39D4D",  # Orange
}

# Ordning som åldersgrupperna ska visas i
ORDNING = ["Barn (0-19)", "Unga (20-39)", "Vuxna (40-64)", "Äldre (65+)"]

# Ordning som åldersgrupperna ska visas i
ORDNING = ["Barn (0-19)", "Unga (20-39)", "Vuxna (40-64)", "Äldre (65+)"]


def styla_donut(fig, total_antal):
    # Stil på själva ringen och segmenten
    fig.update_traces(
        textposition="outside",
        textinfo="percent",
        textfont=dict(size=14),
        marker=dict(line=dict(color="white", width=4)),
        sort=False,
        direction="clockwise",
    )

    # Lägg till totalsumman i mitten av donuten
    fig.add_annotation(
        text=f"<b>{total_antal:,}</b><br><span style='font-size:14px'>Boende</span>",
        x=0.5,
        y=0.5,
        font=dict(size=22, color="#333"),
        showarrow=False,
    )

    # Layout för hela diagrammet
    fig.update_layout(
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="left",
            x=0.3,
        ),
        margin=dict(t=50, b=20, l=20, r=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    return fig