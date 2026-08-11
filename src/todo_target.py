def normalize_status(value):
    return value.strip().lower()


def todo_target(value):
    normalized = normalize_status(value)
    if normalized == "todo":
        return "done"
    return normalized
