def read_from_file(filename: str):
    with open(filename) as f:
        return f.read()


def write_to_file(filename: str, contents: str):
    with open(filename, 'w') as f:
        f.write(contents)


def input_from_console(message: str) -> str:
    return input(message)
