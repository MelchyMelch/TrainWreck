def concat(val1: str, val2: str):
    return val1 + val2


def format_data(value):
    import train_wreck_src.memory as memory

    if not isinstance(value, list):
        try:
            value = float(value)
        except ValueError:
            value = value.replace("Æ¸", " ")

            if value in memory.memory_heap:
                return memory.get_value(value)

    return value
