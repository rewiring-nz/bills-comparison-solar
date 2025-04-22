from enum import Enum
from typing import List, Optional, TypedDict


class Config(TypedDict):
    upfront_cost: float
    interest_rate: float
    years: int
    grid_price: float
    export_tariff: float
    self_consumption: float


DEFAULTS: Config = {
    "upfront_cost": 18000,
    "interest_rate": 5.5,
    "years": 15,
    "grid_price": 0.34,
    "export_tariff": 0.13,
    "self_consumption": 50,
}


AVERAGE_DAILY_POWER_USE = 20  # kWh
AVERAGE_ANNUAL_POWER_USE = AVERAGE_DAILY_POWER_USE * 365.25  # kWh


class ChartSeriesLabel(Enum):
    POWER_BILL = "Power bill"
    UPFRONT_COST = "Upfront cost"
    INTEREST = "Interest"
    PRINCIPAL_REPAYMENTS = "Principal repayments"


CHART_SERIES_COLOURS = {
    ChartSeriesLabel.POWER_BILL: "#FF5733",
    ChartSeriesLabel.UPFRONT_COST: "#3366FF",
    ChartSeriesLabel.INTEREST: "#33CC33",
    ChartSeriesLabel.PRINCIPAL_REPAYMENTS: "#FFCC00",
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
