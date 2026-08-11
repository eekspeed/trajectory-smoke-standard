"""Amortization helpers for the mortgage exercise."""


def monthly_payment(principal, annual_rate, term_months):
    """Return the fixed monthly payment for a loan."""
    if principal <= 0 or annual_rate < 0 or term_months <= 0:
        raise ValueError("invalid loan terms")
    return principal / term_months


def build_schedule(principal, annual_rate, term_months):
    """Build the monthly principal and interest schedule."""
    payment = monthly_payment(principal, annual_rate, term_months)
    return [
        {
            "month": month,
            "payment": round(payment, 2),
            "interest": 0.0,
            "principal": round(payment, 2),
            "balance": round(principal - payment * month, 2),
        }
        for month in range(1, term_months + 1)
    ]
