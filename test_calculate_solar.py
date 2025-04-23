from calculate_solar import calculate_upfront_cost


def test_calculate_upfront_cost():
    expected = round(5 * 20500 / 9)
    assert calculate_upfront_cost(5) == expected
