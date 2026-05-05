# Färger för socioekonomisk radar (BoKoll-paletten)
LINJEFARG_VAL = "#41564D"          # Mörkgrön för valt område
FYLLNAD_VAL = "rgba(65, 86, 77, 0.5)"      # Mörkgrön transparent (matchar linjen)

LINJEFARG_REF = "#E39D4D"          # Orange för Stockholm-referens
FYLLNAD_REF = "rgba(0, 0, 0, 0)"   # Ingen fyllning på Stockholm

# Indikatorer (axlar) med fotnot-asterisker
INDIKATORER = [
    "Ekonomiskt bistånd",
    "Förgymnasial<br>utbildning **",
    "Låg ekonomisk<br>standard *",
]


def styla_radar(fig, max_value):
    # Layout för hela radar-diagrammet
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max_value],
                showline=False,
                gridcolor="rgba(0,0,0,0.1)",
                tickfont=dict(size=10, color="#666"),
                ticksuffix="%",
                angle=90,
                tickangle=90,
            ),
            angularaxis=dict(
                tickfont=dict(size=11, color="#333"),
                rotation=90,
                direction="clockwise",
                gridcolor="rgba(0,0,0,0.1)",
            ),
            bgcolor="rgba(0,0,0,0)",
        ),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            font=dict(size=12),
        ),
        # Mer marginal så texten inte klipps
        margin=dict(t=60, b=80, l=100, r=100),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=450,
    )

    return fig