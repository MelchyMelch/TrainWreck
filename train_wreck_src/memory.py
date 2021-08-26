
memory_heap: {} = {}


def get_value(name: str):
    if name in memory_heap:
        return memory_heap[name]

    try:
        return float(name)
    except ValueError:
        return name


def set_value(value, key):
    try:
        value = float(value)
    except ValueError:
        pass
    memory_heap[key] = value
