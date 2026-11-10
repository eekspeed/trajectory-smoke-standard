"""Public mortgage calculation API."""

from src.amortization import build_schedule, monthly_payment


def calculate_five_year_mortgage(principal, annual_rate):
    """Calculate a fully amortizing five-year mortgage."""
    term_months = 60
    schedule = build_schedule(principal, annual_rate, term_months)
    total_paid = round(sum(row["payment"] for row in schedule), 2)
    total_interest = round(sum(row["interest"] for row in schedule), 2)
    return {
        "monthly_payment": schedule[0]["payment"],
        "total_paid": total_paid,
        "total_interest": total_interest,
        "schedule": schedule,
    }
