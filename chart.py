import plotly.graph_objects as go

from constants import CHART_SERIES_COLOURS, COLOURS, ChartData


def create_stacked_bar_chart(title: str, subtitle: str, data: ChartData, ymax: int):
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
                hovertemplate=f"{label.value}: $%{{y:,.0f}}<extra></extra>",
            )
        )

    fig.update_layout(
        title={
            "text": title,
            "x": 0.0,
            "y": 0.99,
            "xanchor": "left",
            "yanchor": "top",
            "font": {
                "size": 24,
            },
        },
        # Add a subtitle using annotations
        annotations=[
            {
                "text": subtitle,
                "showarrow": False,
                "x": 0.0,
                "y": 1.25,
                "xref": "paper",
                "yref": "paper",
                "xanchor": "left",
                "yanchor": "top",
                "font": {"size": 18, "color": COLOURS["neutral"]["900"]},
            }
        ],
        barmode="stack",
        showlegend=False,
        margin=dict(l=0, r=0, t=60, b=0),
        height=220,
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            tickfont=dict(size=14, color=COLOURS["neutral"]["900"]),
        ),
        yaxis=dict(
            range=[0, ymax],
            showgrid=False,
            showline=False,
            showticklabels=False,
            title=None,
        ),
        plot_bgcolor=COLOURS["neutral"]["50"],
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_color="black",
            font_size=14,
        ),
    )

    return fig
