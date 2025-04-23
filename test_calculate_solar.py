from calculate_solar import calculate_upfront_cost


def test_calculate_upfront_cost():
    assert calculate_upfront_cost(5, 2000) == 10000
