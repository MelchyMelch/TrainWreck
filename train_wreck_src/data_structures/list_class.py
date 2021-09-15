import random
import train_wreck_src.other as other


class List(list):
    def __init__(self, values):
        super().__init__(values)

        self.max_length = random.randint(5, 10)
        self.check_length()

        for i, v in enumerate(self):
            self[i] = other.format_data(v)

    def append(self, __object) -> None:
        super().append(other.format_data(__object))
        self.check_length()

    def check_length(self):
        if len(self) > self.max_length:
            print("Insufficient storage space")
            cc_number = input("Give me your credit card number to upgrade: ")
            if cc_number:
                self.max_length += 5
                print("Successfully upgraded")
                print("Gave 5 new slots for $4154541121.01 + Taxes & V.A.T. & shipping and handling")
                print("Enjoy being broke :)")
            else:
                del self[-1]
                print("Failed to give me money. Last item has been removed.")
    