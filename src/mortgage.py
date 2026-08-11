"""Public mortgage calculation API."""

from src.amortization import build_schedule, monthly_payment


def calculate_five_year_mortgage(principal, annual_rate):
    """Calculate a fully amortizing five-year mortgage."""
    term_months = 60
    schedule = build_schedule(principal, annual_rate, term_months)
    payment = monthly_payment(principal, annual_rate, term_months)
    return {
        "monthly_payment": round(payment, 2),
        "total_paid": round(payment * term_months, 2),
        "total_interest": 0.0,
        "schedule": schedule,
    }
