import string
from typing import List, Optional, TypedDict
from app import Config

AVERAGE_DAILY_POWER_USE = 20  # kWh
AVERAGE_ANNUAL_POWER_USE = AVERAGE_DAILY_POWER_USE * 365.25  # kWh


class ChartSeries(TypedDict):
    label: string
    years: Optional[List[int]]
    bill_values: List[float]


type ChartData = List[ChartSeries]


class ChartDataSet(TypedDict):
    no_solar: ChartData
    with_solar: ChartData
    with_solar_on_finance: ChartData


def calculate(config: Config) -> ChartDataSet:
    no_solar = calculate_no_solar(config["grid_price"], config["years"])
    with_solar = calculate_with_solar(config, no_solar)
    with_solar_on_finance = calculate_with_solar_on_finance(config)
    return ChartDataSet(no_solar, with_solar, with_solar_on_finance)


def calculate_no_solar(grid_price: float, n_years: int) -> ChartData:
    return [
        {
            "label": "Power bill",
            "years": get_years_range(n_years),
            # TODO unit test & confirm
            "bill_values": [AVERAGE_ANNUAL_POWER_USE * grid_price] * n_years,
        }
    ]


def calculate_with_solar(config: Config) -> ChartData:
    years_range = get_years_range(config["years"])
    # TODO: currently just dummy values
    return [
        {
            "label": "Power bill",
            "years": years_range,
            # TODO calculate properly
            "bill_values": [AVERAGE_ANNUAL_POWER_USE * "grid_price"]
            * config["years"]
            * 0.2,
        },
        {
            "label": "Upfront cost",
            "years": years_range,
            "bill_values": [config["upfront_cost"]]
            + [0] * (config["years"] - 1) * config["years"] * 0.2,
        },
    ]


def calculate_with_solar_on_finance(config: Config) -> ChartData:
    years_range = get_years_range(config["years"])
    # TODO: currently just dummy values
    return [
        {
            "label": "Power bill",
            "years": years_range,
            # TODO calculate properly
            "bill_values": [AVERAGE_ANNUAL_POWER_USE * "grid_price"]
            * config["years"]
            * 0.2,
        },
        {
            "label": "Interest",
            "years": years_range,
            # TODO: calculate properly
            "bill_values": [100] * config["years"],
        },
        {
            "label": "Repayments",
            "years": years_range,
            "bill_values": [config["upfront_cost"] / config["years"]] * config["years"],
        },
    ]


def get_years_range(n_years: int) -> List[int]:
    return list(range(1, n_years + 1))
