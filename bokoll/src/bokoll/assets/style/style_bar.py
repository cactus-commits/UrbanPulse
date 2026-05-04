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