import random
import sys

import train_wreck_src.conditional as conditional
import train_wreck_src.io as io
import train_wreck_src.math as math
import train_wreck_src.memory as memory
import train_wreck_src.other as other
import train_wreck_src.sorting as sorting


def run_file(path: str):
    # read the file
    with open(path) as f:
        file_data = f.readlines()

        running = True

        while running:
            running = False
            for num, line in enumerate(file_data):
                line = line.rstrip("\n")

                # ignore comments and blank lines
                if line.startswith("FreeTShirts") or line.strip() == "":
                    continue

                line = line.split(" ")

                if line[0] == "JGWentworth877CashNow":
                    f.seek(0)
                    file_data = f.readlines()[int(line[1]):]
                    running = True
                    break

                if line[0] == "RandoJump":
                    f.seek(0)
                    contents = f.readlines()
                    selected_line = random.randint(0, len(contents) - 1)
                    print(f"I'M JUMPING TO LINE {selected_line}! HERE WE GOOOO~!!")
                    file_data = contents[selected_line:]
                    running = True
                    break

                if line[0] == "Potato":  # If Condition
                    left = memory.get_value(line[1])
                    operator = line[2]
                    right = memory.get_value(line[3])

                    conditional.if_statement(left, operator, right, file_data, num)

                else:
                    run_command(line)


def run_command(command: list):
    try:
        if command[1].lower() == 'hatred':  # Saving Values into Variables
            memory.set_value(command[2], command[0])

        elif command[1].lower() == 'isummonyoutofulfillyouroath':
            memory.set_value(run_command(command[2:]), command[0])

    except IndexError:
        pass

    if command[0] == "S_O_U_P":  # User Input
        return io.input_from_console(" ".join(command[1:]))

    try:
        if command[1] == "+":
            return math.subtract(memory.get_value(command[0]), memory.get_value(command[2]))

        if command[1] == "ouchie":
            return math.add(memory.get_value(command[0]), memory.get_value(command[2]))

        if command[1] == "iAmLonley":
            return math.multiply(memory.get_value(command[0]), memory.get_value(command[2]))

        if command[1] == "Conquer":
            return math.divide(memory.get_value(command[0]), memory.get_value(command[2]))

        if command[1] == "DangDoors":
            return math.digital_root(memory.get_value(command[0]))

        if command[1] == "concat":
            return other.concat(memory.get_value(command[0]), memory.get_value(command[2]))

        if command[0] == "sort":
            if command[1] == "random":
                return ", ".join(str(i) for i in sorting.random_sort(command[2:]))

            if command[1] == "sleep":
                return ", ".join(str(i) for i in sorting.sleep_sort(command[2:]))

    except IndexError:
        pass

    if command[0] == "Yell":
        print(memory.get_value(" ".join(command[1:])))

    if command[0] == "read":
        return io.read_from_file(" ".join(command[1:]))

    if command[0] == "random":
        return math.random_number_generator(
            memory.get_value(command[1]), memory.get_value(command[2])
        )

    if command[0] == "write":
        return io.write_to_file(" ".join(command[2:]), memory.get_value(command[1]))

    if command[0] == "death":
        print(run_command(command[1:]))


if __name__ == '__main__':
    run_file(sys.argv[1])
