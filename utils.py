from constants import ChartData, ChartDataSet


def sum_chart_data_bill_values(data: ChartData) -> float:
    """Returns the sum of all the bill_values in the series contained in the dataset"""
    total_sum = 0.0
    for series in data:
        total_sum += sum(series["bill_values"])
    return round(total_sum)


def get_ymax(data: ChartDataSet) -> int:
    """Get an appropriate ymax so that all charts have the same y-axes for comparability"""
    # Collect all bill values from all series in all datasets
    all_values = []

    for dataset_key in ["no_solar", "with_solar", "with_solar_on_finance"]:
        dataset = data[dataset_key]
        for series in dataset:
            all_values.extend(series["bill_values"])

    # Find the maximum value
    max_value = max(all_values) if all_values else 0

    # Round up to a sensible value for a chart
    # Strategy: round up to the next multiple of an appropriate power of 10
    if max_value == 0:
        return 10  # Default if no data

    # Determine the magnitude of the number
    magnitude = 10 ** (len(str(int(max_value))) - 1)

    # Round up based on the magnitude
    if max_value <= 10:
        # For small values, round up to the next whole number
        return int(max_value) + (1 if max_value > int(max_value) else 0)
    elif max_value <= 100:
        # For values between 10 and 100, round up to the next multiple of 5
        return 5 * (int(max_value / 5) + (1 if max_value % 5 > 0 else 0))
    elif max_value <= 1000:
        # For values between 100 and 1000, round up to the next multiple of 50
        return 50 * (int(max_value / 50) + (1 if max_value % 50 > 0 else 0))
    else:
        # For larger values, round up to the next multiple of the appropriate power of 10
        # divided by 2 (e.g., 500, 5000, etc.)
        nice_interval = magnitude / 2
        return nice_interval * (
            int(max_value / nice_interval) + (1 if max_value % nice_interval > 0 else 0)
        )
