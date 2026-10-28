SHORT_STAY_NIGHTS = 4
LONG_STAY_NIGHTS = 14

STANDARD_DISCOUNT = 0.06
LONG_STAY_DISCOUNT = 0.18

CLEANING_FEE_LIMIT = 300
CLEANING_FEE = 40

CREDIT_CHECK_LIMIT = 2000

WELCOME_MIN_NIGHTS = 5
WELCOME_TOTAL_LIMIT = 1000


def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Calculate the room cost before discounts."""
    return nightly_rate * nights


def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """Return the discount rate for a hotel stay."""
    if nights >= LONG_STAY_NIGHTS:
        return LONG_STAY_DISCOUNT
    elif nights >= SHORT_STAY_NIGHTS or corporate:
        return STANDARD_DISCOUNT
    else:
        return 0.0


def calculate_stay_total(
    nightly_rate: float, nights: int, corporate: bool = False
) -> float:
    """Calculate the stay total after discounts and fees."""
    room_cost = calculate_room_cost(nightly_rate, nights)
    discount = get_stay_discount(nights, corporate)

    discounted_cost = room_cost * (1 - discount)

    if discounted_cost <= CLEANING_FEE_LIMIT:
        discounted_cost += CLEANING_FEE

    return discounted_cost


def requires_credit_check(total: float) -> bool:
    """Return True if the stay requires a credit check."""
    return total >= CREDIT_CHECK_LIMIT


def gets_welcome_package(nights: int, total: float) -> bool:
    """Return True if the guest qualifies for a welcome package."""
    return nights > WELCOME_MIN_NIGHTS and total >= WELCOME_TOTAL_LIMIT


def total_reserved(stays: list) -> float:
    """Return the total amount reserved across all stays."""
    total = 0.0

    for stay in stays:
        stay_total = calculate_stay_total(
            stay["nightly_rate"],
            stay["nights"],
            stay["corporate"],
        )
        total += stay_total

    return total


def largest_stay(stays: list) -> str:
    """Return the guest with the largest stay total."""
    largest_total = -1.0
    largest_guest = ""

    for stay in stays:
        stay_total = calculate_stay_total(
            stay["nightly_rate"],
            stay["nights"],
            stay["corporate"],
        )

        if stay_total > largest_total:
            largest_total = stay_total
            largest_guest = stay["guest"]

    return largest_guest


def format_stay_line(
    guest: str, total: float, credit_check: bool, welcome_package: bool
) -> str:
    """Format a guest's stay information for the report."""
    if credit_check:
        credit = "yes"
    else:
        credit = "no"

    if welcome_package:
        welcome = "yes"
    else:
        welcome = "no"

    return (
        f"{guest}: ${total:.2f} | credit check: {credit} | welcome package: {welcome}"
    )
