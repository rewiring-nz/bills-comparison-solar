from enum import Enum
from typing import List, Optional, TypedDict


class Config(TypedDict):
    solar_size: float
    interest_rate: float
    years: int
    grid_price: float
    export_tariff: float
    self_consumption: float


DEFAULTS: Config = {
    "solar_size": 7,
    "interest_rate": 5.5,
    "years": 15,
    "grid_price": 0.27,  # volume price as of Feb 2025
    "export_tariff": 0.135,
    "self_consumption": 50,
}

COLOURS = {
    "neutral": {
        "0": "#FFFFFF",
        "50": "#FDFAF1",
        "100": "#F8F4E6",
        "900": "#222222",
    },
    "sage": {
        "100": "#E7EFE8",
        "200": "#C2D0C4",
        "300": "#859a8e",
        "500": "#527570",
    },
    "red": {"300": "#d06065", "500": "#9B4E52", "700": "#6D3033"},
    "orange": {"300": "#eb7d57", "500": "#B2674C", "700": "#9b4d32"},
    "yellow": {"300": "#FFC754", "500": "#B2924F"},
    "green": {"300": "#90bc60", "500": "#6B7D58"},
    "blue": {"300": "#5e9bc3", "500": "#5A6D7B"},
    "purple": {"300": "#976aa7", "500": "#6E5E74"},
}

# kWh, from this cell: https://docs.google.com/spreadsheets/d/1N1fpcvTa6erS-CiGmYfRD8Gef6INXPEYHMogA5sbiAw/edit?gid=719309390#gid=719309390&range=F94
# Assumes 1.8 cars, both electrified
AVERAGE_ANNUAL_POWER_USE = 9257
# AVERAGE_ANNUAL_POWER_USE = 4377 # without cars, appliances only

# Takes into account the inverter
SOLAR_COST_PER_KW = 20500 / 9  # $2277.78


class ChartSeriesLabel(Enum):
    POWER_BILL = "Power bill"
    UPFRONT_COST = "Upfront cost"
    INTEREST = "Interest"
    PRINCIPAL_REPAYMENTS = "Principal repayments"


CHART_SERIES_COLOURS = {
    ChartSeriesLabel.POWER_BILL: COLOURS["red"]["300"],
    ChartSeriesLabel.UPFRONT_COST: COLOURS["sage"]["500"],
    ChartSeriesLabel.INTEREST: COLOURS["yellow"]["300"],
    ChartSeriesLabel.PRINCIPAL_REPAYMENTS: COLOURS["sage"]["300"],
}


class ChartSeries(TypedDict):
    label: ChartSeriesLabel
    years: Optional[List[int]]
    bill_values: List[float]


type ChartData = List[ChartSeries]


class ChartDataSet(TypedDict):
    no_solar: ChartData
    with_solar: ChartData
    with_solar_on_finance: ChartData
