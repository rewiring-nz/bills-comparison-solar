import plotly.graph_objects as go

from constants import CHART_SERIES_COLOURS, ChartData


def create_stacked_bar_chart(title: str, data: ChartData):
    fig = go.Figure()

    for series in data:
        label = series["label"]
        values = series["bill_values"]

        color = CHART_SERIES_COLOURS.get(label, "#777777")  # Default grey

        fig.add_trace(
            go.Bar(
                x=series["years"],
                y=values,
                name=label.value,
                marker_color=color,
                hovertemplate=f"{label}: $%{{y:,.0f}}<extra></extra>",
            )
        )

    fig.update_layout(
        title=title,
        barmode="stack",
        showlegend=False,
        margin=dict(l=40, r=40, t=50, b=20),
        height=300,
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            tickfont=dict(size=11),
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            title=None,
        ),
        plot_bgcolor="white",
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
        ),
    )

    return fig
