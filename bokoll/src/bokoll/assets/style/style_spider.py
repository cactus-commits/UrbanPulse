# Färger för spider chart (BoKoll-paletten)
LINJEFARG = "#A2C1C6"     # Ljusblå linje
FYLLNADSFARG = "rgba(162, 193, 198, 0.4)"  # Ljusblå med transparens

# Ordning som åldersgrupperna ska visas i
ORDNING = ["0-9", "10-19", "20-29", "30-39", "40-49",
           "50-59", "60-69", "70-79", "80+"]


def styla_spider(fig):
    # Stil på själva linjen och fyllnaden
    fig.update_traces(
        fill="toself",
        fillcolor=FYLLNADSFARG,
        line=dict(color=LINJEFARG, width=2),
        marker=dict(size=8, color=LINJEFARG),
    )

    # Layout för hela diagrammet
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                showline=False,
                gridcolor="rgba(0,0,0,0.1)",
                tickfont=dict(size=10, color="#666"),
                tickformat="~s",  # ← ÄNDRAT från "," till "~s"
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color="#333"),
                rotation=90,
                direction="clockwise",
                gridcolor="rgba(0,0,0,0.1)",
            ),
            bgcolor="rgba(0,0,0,0)",
        ),
        showlegend=False,
        margin=dict(t=40, b=40, l=40, r=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    return fig