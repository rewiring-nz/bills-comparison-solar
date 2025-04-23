import streamlit as st

from calculate import calculate
from chart import create_stacked_bar_chart
from constants import (
    DEFAULTS,
    ChartDataSet,
    Config,
)
from utils import get_ymax, sum_chart_data_bill_values

st.set_page_config(
    page_title="Solar Lifetime Savings Calculator", page_icon="☀️", layout="wide"
)


st.title("Solar Lifetime Savings Calculator ☀️")
st.markdown(
    "Compare the costs of powering your home with and without solar panels over the lifetime of the panels."
)

st.markdown("---")

show_advanced = st.toggle("Show advanced settings", value=False)

config_cols = st.columns(3)

with config_cols[0]:
    solar_size = st.number_input(
        "Size of solar panels (kW)",
        min_value=2,
        max_value=200,
        value=DEFAULTS["solar_size"],
        step=1,
    )

with config_cols[1]:
    interest_rate = st.number_input(
        "Annual interest rate (%)",
        min_value=0.0,
        max_value=20.0,
        value=DEFAULTS["interest_rate"],
        step=0.25,
    )

with config_cols[2]:
    years = st.number_input(
        "Number of years", min_value=5, max_value=30, value=DEFAULTS["years"], step=5
    )

if show_advanced:
    with config_cols[0]:
        grid_price = st.number_input(
            "Grid price ($/kWh)",
            min_value=0.1,
            max_value=1.0,
            value=DEFAULTS["grid_price"],
            step=0.01,
        )
    with config_cols[1]:
        export_tariff = st.number_input(
            "Export Tariff ($/kWh)",
            min_value=0.0,
            max_value=1.0,
            value=DEFAULTS["export_tariff"],
            step=0.01,
        )
    with config_cols[2]:
        self_consumption = st.slider(
            "Self-consumption rate (%)",
            min_value=0,
            max_value=100,
            value=DEFAULTS["self_consumption"],
            step=5,
        )
else:
    grid_price = DEFAULTS["grid_price"]
    export_tariff = DEFAULTS["export_tariff"]
    self_consumption = DEFAULTS["self_consumption"]


# Calculate chart values
config: Config = {
    "solar_size": solar_size,
    "interest_rate": interest_rate,
    "years": years,
    "grid_price": grid_price,
    "export_tariff": export_tariff,
    "self_consumption": self_consumption,
}
chart_data_set: ChartDataSet = calculate(config)

st.markdown("---")

# # Legend
# legend_cols = st.columns(4)
# with legend_cols[0]:
#     st.markdown(
#         f'<div style="background-color:{CHART_SERIES_COLOURS[ChartSeriesLabel.POWER_BILL]}; width:20px; height:20px; display:inline-block; margin-right:10px;"></div> {ChartSeriesLabel.POWER_BILL.value}',
#         unsafe_allow_html=True,
#     )
# with legend_cols[1]:
#     st.markdown(
#         f'<div style="background-color:{CHART_SERIES_COLOURS[ChartSeriesLabel.solar_size]}; width:20px; height:20px; display:inline-block; margin-right:10px;"></div> {ChartSeriesLabel.solar_size.value}',
#         unsafe_allow_html=True,
#     )
# with legend_cols[2]:
#     st.markdown(
#         f'<div style="background-color:{CHART_SERIES_COLOURS[ChartSeriesLabel.PRINCIPAL_REPAYMENTS]}; width:20px; height:20px; display:inline-block; margin-right:10px;"></div> {ChartSeriesLabel.PRINCIPAL_REPAYMENTS.value}',
#         unsafe_allow_html=True,
#     )
# with legend_cols[3]:
#     st.markdown(
#         f'<div style="background-color:{CHART_SERIES_COLOURS[ChartSeriesLabel.INTEREST]}; width:20px; height:20px; display:inline-block; margin-right:10px;"></div> {ChartSeriesLabel.INTEREST.value}',
#         unsafe_allow_html=True,
#     )

# st.markdown("####")  # vertical spacer

# Chart styling
ymax = get_ymax(chart_data_set)

# Chart 1: No Solar
no_solar_total = sum_chart_data_bill_values(chart_data_set["no_solar"])
fig1 = create_stacked_bar_chart(
    title=f"No solar",
    subtitle=f"${no_solar_total:,} total in power bills over {config["years"]} years",
    data=chart_data_set["no_solar"],
    ymax=ymax,
)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# Chart 2: With Solar
with_solar_total = sum_chart_data_bill_values(chart_data_set["with_solar"])
with_solar_savings = no_solar_total - with_solar_total
fig2 = create_stacked_bar_chart(
    title=f"With solar",
    subtitle=f"${with_solar_total:,} total in upfront cost + reduced power bills (${with_solar_savings:,} saved) over {config["years"]} years",
    data=chart_data_set["with_solar"],
    ymax=ymax,
)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Chart 3: With Solar on finance
with_solar_finance_total = sum_chart_data_bill_values(
    chart_data_set["with_solar_on_finance"]
)
with_solar_finance_savings = no_solar_total - with_solar_finance_total
fig3 = create_stacked_bar_chart(
    title=f"With solar on finance at {config["interest_rate"]}% interest p.a.",
    subtitle=f"${with_solar_finance_total:,} total in repayments, interest, and reduced power bills (${with_solar_finance_savings:,} saved) over {config["years"]} years",
    data=chart_data_set["with_solar_on_finance"],
    ymax=ymax,
)
st.plotly_chart(fig3, use_container_width=True)


st.markdown("---")
st.caption(
    "Created by [Rewiring Aotearoa](https://www.rewiring.nz/), a nonprofit representing everyday New Zealanders in the energy transition. [See our open-source model on GitHub](https://github.com/rewiring-nz/bills-comparison-solar). Whakahiko te ao! (Electrify everything!) ⚡️"
)
