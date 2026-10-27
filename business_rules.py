def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Calculate the room cost before discounts."""
    return nightly_rate * nights


def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """Return the discount rate for a hotel stay."""
    if nights >= 14:
        return 0.18
    elif nights >= 4 or corporate:
        return 0.06
    else:
        return 0.0


def calculate_stay_total(
    nightly_rate: float, nights: int, corporate: bool = False
) -> float:
    """Calculate the stay total after discounts and fees."""
    room_cost = calculate_room_cost(nightly_rate, nights)
    discount = get_stay_discount(nights, corporate)

    discounted_cost = room_cost * (1 - discount)

    if discounted_cost <= 300:
        discounted_cost += 40

    return discounted_cost


def requires_credit_check(total: float) -> bool:
    """Return True if the stay requires a credit check."""
    return total >= 2000


def gets_welcome_package(nights: int, total: float) -> bool:
    """Return True if the guest qualifies for a welcome package."""
    return nights > 5 and total >= 1000


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
    credit = "yes" if credit_check else "no"
    welcome = "yes" if welcome_package else "no"

    return (
        f"{guest}: ${total:.2f} | credit check: {credit} | welcome package: {welcome}"
    )
