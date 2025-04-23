import unittest
from unittest.mock import patch
from calculate_solar import calculate_upfront_cost, get_e_generated_from_solar


def test_calculate_upfront_cost():
    assert calculate_upfront_cost(5, 2000) == 10000


def test_get_e_generated_from_solar():
    with patch("calculate_solar.SOLAR_AVG_DEGRADED_PERFORMANCE_30_YRS", 0.8):
        # Test case 1: size=50, capacity=0.15
        result = get_e_generated_from_solar(50, 0.15)
        expected = 50 * 0.15 * 0.8 * 24 * 365.25
        assert result == expected

        # Test case 2: size=200, capacity=0.25
        result = get_e_generated_from_solar(200, 0.25)
        expected = 200 * 0.25 * 0.8 * 24 * 365.25
        assert result == expected

        # Test case 3: size=1000, capacity=0.18
        result = get_e_generated_from_solar(1000, 0.18)
        expected = 1000 * 0.18 * 0.8 * 24 * 365.25
        assert result == expected

        # Test case 4: size=0.5, capacity=0.22
        result = get_e_generated_from_solar(0.5, 0.22)
        expected = 0.5 * 0.22 * 0.8 * 24 * 365.25
        assert result == expected
