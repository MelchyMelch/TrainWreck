import train_wreck_src.other as other

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
    memory_heap[key] = other.format_data(value)
