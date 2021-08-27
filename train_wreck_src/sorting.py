import random
import datetime
import threading
import time

import train_wreck_src.memory as memory


def random_sort(data: list):
    data = [int(i) for i in data]

    sorted_data = data[:]
    sorted_data.sort()

    start = datetime.datetime.now()
    print(f"Pre-Sorted: {', '.join(str(i) for i in data)}")
    while data != sorted_data:
        random.shuffle(data)

    print(f"It took {datetime.datetime.now() - start}")
    print(f"Post-Sorted: {', '.join(str(i) for i in data)}")
    return data


def sleep_sort(data: list):
    sorted_data = []
    threads = []

    def sleep_delay(delay: float):
        time.sleep(delay)
        sorted_data.append(delay)

    for i in data:
        t = threading.Thread(target=sleep_delay, args=[memory.get_value(i)])
        t.setDaemon(True)
        t.start()
        threads.append(t)

    while True:
        for t in threads:
            if t.is_alive():
                break

        else:
            break

    return sorted_data
