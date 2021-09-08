import train_wreck_src.memory as memory


def if_statement(value_1, comparison_operator: str, value_2, file_data: list, num: int):
    # import is here to avoid a circular import
    # PEP8 allows imports to be in functions like this.
    # Especially if it is the WAY more memory efficient "import" instead of the "from ... import"
    import train_wreck

    operator = operator_map[comparison_operator]

    value_1 = memory.get_value(value_1)
    value_2 = memory.get_value(value_2)

    # TODO Clean this up a bit more
    if operator(value_1, value_2):
        line_offset = 1
        while file_data[num + line_offset].startswith("NOTThis"):
            train_wreck.run_command(file_data[num + line_offset].rstrip("\n").lstrip("NOTThis ").split(" "))
            line_offset += 1

    else:
        line_offset = 1
        while file_data[num + line_offset].rstrip("\n") != "FrenchFry":
            line_offset += 1

        line_offset += 1

        try:
            while file_data[num + line_offset].startswith("NOTThis"):
                train_wreck.run_command(file_data[num + line_offset].rstrip("\n").lstrip("NOTThis ").split(" "))
                line_offset += 1
        except IndexError:
            pass


def equals(value_1, value_2):
    return value_1 == value_2


def not_equals(value_1, value_2):
    return value_1 != value_2


def less_than(value_1, value_2):
    return value_1 < value_2


def less_than_equal(value_1, value_2):
    return value_1 <= value_2


def greater_than(value_1, value_2):
    return value_1 > value_2


def greater_than_equal(value_1, value_2):
    return value_1 >= value_2


operator_map = {
    "ghostbusters2016": equals,
    "elephant": not_equals,
    ">": less_than,
    "regret": greater_than,
    "terminatethemate": less_than_equal,
    "PlantPlants": greater_than_equal
}
