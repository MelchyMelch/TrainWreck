import sys

memory_heap = {}


def run_file(path: str):

    with open(path) as f:
        file_data = f.readlines()
        running = True

        while running:
            running = False
            for num, line in enumerate(file_data):
                line = line.rstrip("\n")

                if line.startswith("FreeTShirts") or line.strip() == "":  # Implementing Comments
                    continue

                line = line.split(" ")

                if line[0] == "JGWentworth877CashNow":
                    f.seek(0)
                    file_data = f.readlines()[int(line[1]):]
                    running = True
                    break

                if line[0] == "Potato":  # If Condition
                    left = get_value(line[1])
                    operator = line[2]
                    right = get_value(line[3])

                    passed = False
                    if operator == "ghostbusters2016":  # Equality Operator
                        passed = left == right  # User Input

                    elif operator == "elephant":
                        passed = left != right  # User Input

                    if passed:
                        line_offset = 1
                        while file_data[num + line_offset].startswith("NOTThis"):
                            run_command(file_data[num + line_offset].rstrip("\n").lstrip("NOTThis ").split(" "))
                            line_offset += 1

                    else:
                        line_offset = 1
                        while file_data[num + line_offset].rstrip("\n") != "FrenchFry":
                            line_offset += 1

                        line_offset += 1

                        while file_data[num + line_offset].startswith("NOTThis"):
                            run_command(file_data[num + line_offset].rstrip("\n").lstrip("NOTThis ").split(" "))
                            line_offset += 1

                else:
                    run_command(line)


def get_value(name: str):
    if name in memory_heap:
        return memory_heap[name]
    try:
        return float(name)
    except ValueError:
        return name


def run_command(command: list):
    # print(command)
    try:
        if command[1].lower() == 'hatred':  # Saving Values into Variables
            value = command[2]
            try:
                value = float(value)
            except ValueError:
                pass

            memory_heap[command[0]] = value

        elif command[1].lower() == 'isummonyoutofulfillyouroath':
            value = run_command(command[2:])
            try:
                value = float(value)

            except ValueError:
                pass

            memory_heap[command[0]] = value

    except IndexError:
        pass

    if command[0] == "S_O_U_P": # User Input
        return input(" ".join(command[1:]))

    try:
        if command[1] == "+":
            return get_value(command[0]) - get_value(command[2])

        if command[1] == "ouchie":
            return get_value(command[0]) + get_value(command[2])
    except IndexError:
        pass

    if command[0] == "Yell":
        print(get_value(" ".join(command[1:])))

    if command[0] == "death":
        print(run_command(command[1:]))


if __name__ == '__main__':
    run_file(sys.argv[1])
