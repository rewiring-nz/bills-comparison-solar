from calculate import calculate_no_solar, get_years_range


def test_get_years_range():
    assert get_years_range(5) == [1, 2, 3, 4, 5]


def test_calculate_no_solar():
    result = calculate_no_solar(0.2, 3)
    assert result == [
        {
            "label": "Power bill",
            "years": [1, 2, 3],
            "bill_values": [1461, 1461, 1461],
        }
    ]
