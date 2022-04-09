import time

Scale = 1000000


def run():
    last = time.time()

    while True:
        current = time.time()
        delta_time = current - last

        update(delta_time)
        last = current


def update(delta_time):
    print(delta_time * Scale)


def fixed_update(delta_time):
    return
    print("---", delta_time * 1000)
