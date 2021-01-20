"""
Programmatically generate the altair plots from the notebooks
and save in Reports/Figures.

Author: Tom Fleet
Created: 09/01/2021
"""

import altair as alt
from altair_saver import save

from src.config import FIGURES, MONTHS, TOP_10_COUNTRIES, TOP_10_MANUFACTURERS
from src.data.load_data import Data

# Load the dataset

df = Data().load(clean=True)
top_10_countries_df = df[df["country"].isin(TOP_10_COUNTRIES)]
top_10_manufacturers_df = df[df["manufacturer"].isin(TOP_10_MANUFACTURERS)]


def png_name(fig: alt.Chart) -> str:
    """
    Takes an altair chart, extracts the title and converts this
    to a filename with a .png extension for saving.
    Args:
        fig (alt.Chart): Altair chart object to convert.
    Returns:
        str: Formatted filename (png).
    """

    if fig.title:
        fname = (
            fig.title.strip()
            .replace(" ", "_")
            .replace("-", "")
            .replace(":", "")
            .lower()
            + ".png"
        )
    else:
        raise ValueError("In order to save the chart, it must have a title!")

    return fname


def save_altair_plot(fig: alt.Chart) -> None:

    fname = png_name(fig)

    save(
        chart=fig,
        fp=str(FIGURES.joinpath(fname)),
        fmt="png",
        method="selenium",
        scale_factor=6.0,
    )


fig1 = (
    alt.Chart(
        df.groupby(by="country")[["fatalities"]]
        .sum()
        .nlargest(10, "fatalities")
        .reset_index()
    )
    .mark_bar()
    .encode(
        x=alt.X("country:N", title="Country", sort="-y"),
        y=alt.Y("fatalities:Q", title="Total Fatalities"),
    )
    .properties(title="Total Fatalities by Country (Top 10)", height=500, width=750)
    .configure_axisX(labelAngle=-40)
)

fig2 = (
    alt.Chart(
        top_10_countries_df.groupby("country")
        .mean()
        .sort_values(by="fatality_pct", ascending=False)
        .dropna()
        .reset_index()
    )
    .mark_bar()
    .encode(
        x=alt.X("country:N", title="Country", sort="-y"),
        y=alt.Y(
            "fatality_pct:Q", title="Crash Fatality Rate", axis=alt.Axis(format="%")
        ),
        color=alt.Color("fatality_pct:Q", title=None, scale=alt.Scale(scheme="blues")),
    )
    .properties(title="Mean Crash Fatality Rate by Country", height=500, width=750)
    .configure_axisX(labelAngle=-40)
)

fig3 = (
    alt.Chart(df)
    .mark_bar(opacity=0.4)
    .encode(
        x=alt.X("month:N", title="Month", sort=MONTHS),
        y=alt.Y("sum(fatalities):Q", title="Total Fatalities", stack=None),
        color=alt.Color("sector:N", title="Sector"),
    )
    .properties(title="Total Fatalities by Month", height=500, width=750)
    .configure_axisX(labelAngle=-40)
)

fig4 = (
    alt.Chart(df)
    .mark_line(interpolate="basis")
    .encode(
        x=alt.X("year(date):T", title="Year"),
        y=alt.Y(
            "mean(fatality_pct):Q", title="Fatality Rate", axis=alt.Axis(format="%")
        ),
        color=alt.Color("sector:N", title="Sector"),
    )
    .properties(title="Crash Fatality Rate by Year and Sector", width=750, height=500)
)

fig5 = (
    alt.Chart(df)
    .mark_bar(opacity=0.6)
    .encode(
        x=alt.X("fatality_pct:Q", title="Crash Fatality Rate", bin=alt.Bin(maxbins=10)),
        y=alt.Y("count()", stack=None),
        color=alt.Color("sector:N", title="Sector"),
    )
    .properties(title="Crash Fatality Rate Distribution", height=500, width=750)
)

fig6 = (
    alt.Chart(df[df["fatality_pct"] < 1])
    .mark_bar(opacity=0.6)
    .encode(
        x=alt.X("fatality_pct:Q", title="Crash Fatality Rate", bin=alt.Bin(maxbins=20)),
        y=alt.Y("count()", stack=None),
        color=alt.Color("sector:N", title="Sector"),
    )
    .properties(
        title="Crash Fatality Rate Distribution (Crashes with Fatality Rate < 1)",
        height=500,
        width=750,
    )
)

fig7 = (
    alt.Chart(df.groupby("manufacturer").sum().nlargest(10, "fatalities").reset_index())
    .mark_bar()
    .encode(
        x=alt.X("manufacturer:N", title="Manufacturer", sort="-y"),
        y=alt.Y("fatalities:Q", title="Fatalities"),
    )
    .properties(title="Fatalities by Aircraft Manufacturer", width=750, height=500)
    .configure_axisX(labelAngle=-40)
)

fig8 = (
    alt.Chart(
        top_10_manufacturers_df.groupby("manufacturer")
        .mean()
        .sort_values(by="fatality_pct", ascending=False)
        .dropna()
        .reset_index()
    )
    .mark_bar()
    .encode(
        x=alt.X("manufacturer:N", title="Manufacturer", sort="-y"),
        y=alt.Y(
            "fatality_pct:Q", title="Crash Fatality Rate", axis=alt.Axis(format="%")
        ),
        color=alt.Color("fatality_pct:Q", title=None, scale=alt.Scale(scheme="blues")),
    )
    .properties(
        title="Mean Crash Fatality Rate by Aircraft Manufacturer", height=500, width=750
    )
    .configure_axisX(labelAngle=-40)
)


if __name__ == "__main__":
    figs = [fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8]
    for fig in figs:
        save_altair_plot(fig)
        print(f"Figure: {png_name(fig)} saved successfuly!")
