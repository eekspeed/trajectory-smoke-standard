"""Basic statistics helpers used by the reporting module."""


def mean(values):
    """Return the arithmetic mean of a non-empty sequence."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def median(values):
    """Return the median of a non-empty sequence."""
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2
