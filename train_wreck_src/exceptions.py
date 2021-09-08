import enum
import random

from colorama import Fore, init

init(autoreset=True)


class ErrorType(enum.Enum):
    ThinkingCan = "ThinkingCan"
    Sparky = "Sparky"
    YouDidItYay = "YouDidItYay"
    FailedSuccessfully = "FailedSuccessfully"
    hahaSTINKY = "hahaSTINKY"


def raise_exception(message: ErrorType):
    print("Error Code " + get_color() + message.value + Fore.RESET + ". " + get_random_fact())
    quit(-1)


def get_color():
    return random.choice([
        Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
    ])


def get_random_fact() -> str:
    return random.choice([
        "Polar bears are left handed",
        "It is illegal to go fishing on a giraffe in Nevada",
        "No you can't have the rest of my sandwich",
        "the airbnb of tiktok",
        "Why did we make this?",
        "the uber of facebook",
        "Competitive art used to be in the Olympics.",
        '"OMG" usage can be traced back to 1917.',
        "Some cats are actually allergic to humans.",
        "The majority of your brain is fat.",
        "Oranges aren't naturally occurring fruits.",
        "High heels were originally worn by men.",
        "Stop signs used to be yellow.",
        "MelchyMelch's internet is poop",
        "New York was briefly named \"New Orange.\"",
        "There was a successful Tinder match in Antarctica in 2014.",
        "Most wasabi we eat in the U.S. isn't really wasabi.",
        "Amelia Earhart and Eleanor Roosevelt once went on a joyride.",
        "Green Eggs and Ham started as a bet.",
        "Metallica was the first band to play a concert in all 7 continents",
        "Sound Alerts is currently disabled :( Please enable it on ***",
        "Too much water can kill you.",
        "The moon is (slowly) slowing the Earth's rotation.",
        "You might be drinking water that is older than the solar system.",
        "Queen Elizabeth II is a trained mechanic.",
        "\n⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n"
        "⬛⬛🔴🔴🔴🔴⬛🔴⬛⬛🔴⬛🔴🔴🔴🔴⬛⬛ \n"
        "⬛⬛🔴⬛⬛⬛⬛🔴⬛⬛🔴⬛🔴⬛⬛⬛⬛⬛ \n"
        "⬛⬛🔴🔴🔴🔴⬛🔴⬛⬛🔴⬛🔴🔴🔴🔴⬛⬛ \n"
        "⬛⬛⬛⬛⬛🔴⬛🔴⬛⬛🔴⬛⬛⬛⬛🔴⬛⬛ \n"
        "⬛⬛🔴🔴🔴🔴⬛⬛🔴🔴⬛⬛🔴🔴🔴🔴⬛⬛ \n"
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "It takes 364 licks to get to the center of a Tootsie Pop.",
        "\n⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⢉⣉⣉⣉⣉⡛⠛⠛⠛⠛⠛⠛⠻⠻⠿⠿⣿⣿⣿⣿ \n"
        "⣿⣿⣿⣿⠟⠋⠉⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⠀⠁⠀⠄⠀⠄⠀⠌⠉⠛ \n"
        "⣟⠉⠁⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠐⠀⠐⠀⠐⠀ \n"
        "⡟⠀⠀⠀⠒⠋⠉⠉⠈⠀⠉⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠈⢀⠈⠀⠄ \n"
        "⠀⠀⠀⠀⣀⣴⠖⢁⣠⣶⣶⣶⣦⣴⣿⣿⣻⣾⣿⣾⣿⣻⣿⣿⣿⣧⠀⠀⡀⠂⠀ ⠀\n"
        "⣀⣰⣾⡿⠁⢠⣻⣽⣿⣟⣿⣟⣿⣿⣽⣿⢿⣷⡿⣟⣿⣷⣷⠹⣿⡆⠀⠀⡀⠁ \n"
        "⠘⣿⣿⡟⠁⠀⡾⣽⣿⣯⣿⣿⣻⣿⣽⣿⣽⣿⡿⣿⣿⢿⣻⣾⡀⠸⣯⠀⠀⠀⠄ ⠀\n"
        "⣺⡿⠀⠀⢨⣟⣿⣽⣯⣿⣾⣿⣿⣽⣿⣽⣿⢿⣟⣿⣿⣿⣿⡿⡆⠈⠀⠀⠂⠀ ⠀\n"
        "⢺⡯⠀⠀⣼⢾⢻⠿⠻⠿⠽⣷⣿⣯⣿⠿⠚⠛⠙⠉⢈⣀⠠⠌⣀⠀⡀⠀⢀⠁ ⠀⠈\n"
        "⠟⢀⣀⢈⣀⠄⢀⢤⠀⠀⠀⠉⣉⣌⠀⢀⠀⠊⢑⣒⠈⠀⣸⣿⡀⣿⡀⠀⡀ ⠀⠀⢰⡆\n"
        "⠀⠈⠁⠂⣩⣤⣤⣤⡀⠀⣾⣿⣦⣼⣿⣾⣿⢿⡾⢀⣿⣟⣿⡯⠂⠀⡀ ⠀⠀⠀⠑⠀⠀\n"
        "⠹⣶⣿⣿⣿⣿⠋⢀⣷⣿⣟⣿⡯⢿⢾⣿⣷⣾⣿⣻⣿⠃⠀⢀⠀ ⠀⠀⠀⠀⠀⠀⠐\n"
        "⣤⡿⣿⡾⠂⠰⡅⠓⡿⣿⡻⠃⣄⠈⠚⣽⣾⡿⣟⠛⠀⠀⠄⠀ ⠀⠄⠀⠀⠀⠀⠀⠀\n"
        "⠙⠁⠀⠀⠀⣤⣤⣀⣀⣴⣿⣿⣷⣤⡀⢸⣿⡇⠀⠀⠐⠈⣿ ⠀⠀⠂⠀⠀⠀⠀⠀⢰⡦\n"
        "⠀⠐⠟⠋⠉⠉⣁⣀⣀⠀⠀⠀⠀⣰⣿⡧⠀⠐⠀⢼⣿ ⠀⠁⡀⠂⠀⠀⠀⠀⠹⣽⡄⠀\n"
        "⠀⠀⠀⣉⣥⣤⣦⣶",
        "The blob of toothpaste that sits on your toothbrush is called a \"nurdle\"",
        "The end of a shoelace is called an aglet"
    ])
