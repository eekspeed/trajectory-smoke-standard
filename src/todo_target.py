def normalize_status(value):
    return value


def todo_target(value):
    normalized = normalize_status(value)
    if normalized == "todo":
        return "done"
    return normalized
