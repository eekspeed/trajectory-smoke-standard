"""Amortization helpers for the mortgage exercise."""


def monthly_payment(principal, annual_rate, term_months):
    """Return the fixed monthly payment for a loan."""
    if principal <= 0 or annual_rate < 0 or term_months <= 0:
        raise ValueError("invalid loan terms")
    monthly_rate = annual_rate / 12
    if monthly_rate == 0:
        return principal / term_months
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -term_months)


def build_schedule(principal, annual_rate, term_months):
    """Build the monthly principal and interest schedule."""
    payment = round(monthly_payment(principal, annual_rate, term_months), 2)
    monthly_rate = annual_rate / 12
    balance = round(principal, 2)
    schedule = []
    for month in range(1, term_months + 1):
        interest = round(balance * monthly_rate, 2)
        principal_paid = round(payment - interest, 2)
        if month == term_months:
            principal_paid = balance
            payment_for_month = round(principal_paid + interest, 2)
        else:
            payment_for_month = payment
        balance = round(balance - principal_paid, 2)
        schedule.append(
            {
                "month": month,
                "payment": payment_for_month,
                "interest": interest,
                "principal": principal_paid,
                "balance": balance,
            }
        )
    return schedule
