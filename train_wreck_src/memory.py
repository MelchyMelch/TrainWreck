
memory_heap: {} = {}


def get_value(name: str):
    if name in memory_heap:
        value = memory_heap[name]

        if isinstance(value, str):
            value = value.replace("Æ¸", " ")

        return value

    try:
        return float(name)
    except ValueError:
        return name.replace("Æ¸", " ")


def set_value(value, key):
    try:
        value = float(value)
    except ValueError:
        value = value.replace("Æ¸", " ")
    memory_heap[key] = value
