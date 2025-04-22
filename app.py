import streamlit as st

st.set_page_config(page_title="Solar Cost Comparison", page_icon="☀️", layout="wide")


st.title("Solar Energy Cost Comparison")
st.markdown(
    "Compare the costs of powering your home with and without solar panels over time."
)

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# Main settings
with col1:
    upfront_cost = st.number_input(
        "Cost of solar panels ($)",
        min_value=1000,
        max_value=50000,
        value=18000,
        step=1000,
    )

with col2:
    interest_rate = st.number_input(
        "Annual interest rate (%)", min_value=0.0, max_value=20.0, value=5.5, step=0.25
    )

with col3:
    years = st.number_input(
        "Number of years", min_value=5, max_value=30, value=15, step=1
    )

# Advanced settings (hidden by default)

with col4:
    show_advanced = st.checkbox("Show advanced settings")

if show_advanced:
    with col1:
        grid_price = st.number_input(
            "Grid price ($/kWh)", min_value=0.1, max_value=1.0, value=0.34, step=0.01
        )
    with col2:
        export_tariff = st.number_input(
            "Export Tariff ($/kWh)", min_value=0.0, max_value=1.0, value=0.13, step=0.01
        )
    with col3:
        self_consumption = st.slider(
            "Self-consumption rate (%)", min_value=0, max_value=100, value=50, step=5
        )
