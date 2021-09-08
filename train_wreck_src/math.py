import random
import train_wreck_src.exceptions as exceptions


def add(val1, val2):
    return val1 + val2


def subtract(val1, val2):
    return val1 - val2


def multiply(val1, val2):
    return val1 * val2


def divide(val1, val2):
    try:
        return val1 / val2
    except ZeroDivisionError:
        exceptions.raise_exception(exceptions.ErrorType.Sparky)


def digital_root(value):
    # 156 -> 1 + 5 + 6 = 12 -> 1 + 2 = 3 --> digital_root(156) is 3
    return (value - 1) % 9 + 1 if value else 0


def random_number_generator(maximum, minimum):
    return random.randint(maximum, minimum)
