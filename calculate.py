from typing import List

from constants import (
    AVERAGE_ANNUAL_POWER_USE,
    ChartData,
    ChartDataSet,
    ChartSeriesLabel,
    Config,
)


def calculate(config: Config) -> ChartDataSet:
    no_solar = calculate_no_solar(config["grid_price"], config["years"])
    with_solar = calculate_with_solar(config)
    with_solar_on_finance = calculate_with_solar_on_finance(config)
    return ChartDataSet(
        {
            "no_solar": no_solar,
            "with_solar": with_solar,
            "with_solar_on_finance": with_solar_on_finance,
        }
    )


def calculate_no_solar(grid_price: float, n_years: int) -> ChartData:
    return [
        {
            "label": ChartSeriesLabel.POWER_BILL,
            "years": format_years_range(get_years_range(n_years)),
            # TODO unit test & confirm
            "bill_values": [AVERAGE_ANNUAL_POWER_USE * grid_price] * n_years,
        }
    ]


def calculate_with_solar(config: Config) -> ChartData:
    years_range = format_years_range(get_years_range(config["years"]))
    # TODO: currently just dummy values
    return [
        {
            "label": ChartSeriesLabel.POWER_BILL,
            "years": years_range,
            # TODO calculate properly
            "bill_values": [AVERAGE_ANNUAL_POWER_USE * config["grid_price"] * 0.2]
            * config["years"],
        },
        {
            "label": ChartSeriesLabel.UPFRONT_COST,
            "years": years_range,
            "bill_values": [config["upfront_cost"]] + [0] * (config["years"] - 1),
        },
    ]


def calculate_with_solar_on_finance(config: Config) -> ChartData:
    years_range = format_years_range(get_years_range(config["years"]))
    # TODO: currently just dummy values
    return [
        {
            "label": ChartSeriesLabel.POWER_BILL,
            "years": years_range,
            # TODO calculate properly
            "bill_values": [AVERAGE_ANNUAL_POWER_USE * config["grid_price"] * 0.2]
            * config["years"],
        },
        {
            "label": ChartSeriesLabel.INTEREST,
            "years": years_range,
            # TODO: calculate properly
            "bill_values": [100] * config["years"],
        },
        {
            "label": ChartSeriesLabel.PRINCIPAL_REPAYMENTS,
            "years": years_range,
            "bill_values": [config["upfront_cost"] / config["years"]] * config["years"],
        },
    ]


def get_years_range(n_years: int) -> List[int]:
    return list(range(1, n_years + 1))


def format_years_range(years_list: List[int]) -> List[str]:
    return [f"Year {i}" for i in years_list]
