from business_rules import (
    calculate_room_cost,
    calculate_stay_total,
    format_stay_line,
    get_stay_discount,
    gets_welcome_package,
    largest_stay,
    requires_credit_check,
    total_reserved,
)


def test_room_cost_two_nights():
    assert round(calculate_room_cost(100, 2), 2) == 200.00


def test_room_cost_five_nights():
    assert round(calculate_room_cost(150, 5), 2) == 750.00


def test_room_cost_one_night():
    assert round(calculate_room_cost(125, 1), 2) == 125.00


def test_discount_three_nights():
    assert get_stay_discount(3) == 0.0


def test_discount_four_nights():
    assert get_stay_discount(4) == 0.06


def test_discount_thirteen_nights():
    assert get_stay_discount(13) == 0.06


def test_discount_fourteen_nights():
    assert get_stay_discount(14) == 0.18


def test_discount_corporate_guest():
    assert get_stay_discount(2, True) == 0.06


def test_cleaning_fee_below_limit():
    assert round(calculate_stay_total(100, 2), 2) == 240.00


def test_cleaning_fee_at_limit():
    assert round(calculate_stay_total(150, 2), 2) == 340.00


def test_no_cleaning_fee_above_limit():
    assert round(calculate_stay_total(150.50, 2), 2) == 301.00


def test_stay_total_with_discount():
    assert round(calculate_stay_total(100, 5), 2) == 470.00


def test_credit_check_below_limit():
    assert requires_credit_check(1999.99) is False


def test_credit_check_at_limit():
    assert requires_credit_check(2000) is True


def test_welcome_package_five_nights():
    assert gets_welcome_package(5, 1200) is False


def test_welcome_package_six_nights():
    assert gets_welcome_package(6, 1200) is True


def test_welcome_package_below_total_limit():
    assert gets_welcome_package(6, 999.99) is False


def test_welcome_package_at_total_limit():
    assert gets_welcome_package(6, 1000) is True


def test_total_reserved_two_stays():
    stays = [
        {"guest": "Alex", "nightly_rate": 100, "nights": 2, "corporate": False},
        {"guest": "Sam", "nightly_rate": 150, "nights": 2, "corporate": False},
    ]

    assert round(total_reserved(stays), 2) == 580.00


def test_total_reserved_empty_list():
    assert total_reserved([]) == 0.0


def test_largest_stay_two_guests():
    stays = [
        {"guest": "Alex", "nightly_rate": 100, "nights": 2, "corporate": False},
        {"guest": "Sam", "nightly_rate": 200, "nights": 5, "corporate": False},
    ]

    assert largest_stay(stays) == "Sam"


def test_largest_stay_tie():
    stays = [
        {"guest": "Alex", "nightly_rate": 100, "nights": 2, "corporate": False},
        {"guest": "Sam", "nightly_rate": 100, "nights": 2, "corporate": False},
    ]

    assert largest_stay(stays) == "Alex"


def test_largest_stay_empty_list():
    assert largest_stay([]) == ""


def test_format_stay_line_with_yes_values():
    result = format_stay_line("Alex", 1200, True, True)
    assert result == "Alex: $1200.00 | credit check: yes | welcome package: yes"


def test_format_stay_line_with_no_values():
    result = format_stay_line("Sam", 250, False, False)
    assert result == "Sam: $250.00 | credit check: no | welcome package: no"
