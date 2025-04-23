from calculate import calculate_no_solar, calculate_with_solar, get_years_range
from constants import ChartSeriesLabel, Config


def test_get_years_range():
    assert get_years_range(5) == [1, 2, 3, 4, 5]


def test_calculate_no_solar():
    result = calculate_no_solar(0.2, 3)
    assert result == [
        {
            "label": ChartSeriesLabel.POWER_BILL,
            "years": ["Year 1", "Year 2", "Year 3"],
            "bill_values": [1461.0, 1461.0, 1461.0],
        }
    ]


# def test_calculate_with_solar():
#     config: Config = {
#         "solar_size": 1,
#         "interest_rate": 1,
#         "years": 1,
#         "grid_price": 1,
#         "export_tariff": 1,
#         "self_consumption": 1,
#     }
#     result = calculate_with_solar(config)
