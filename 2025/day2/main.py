import math


def read_to_string(path):
    with open(path) as f:
        string = f.read()
        return string


def read_to_list(path):
    with open(path) as f:
        lines = f.read().splitlines()
        return lines


def is_invalid(num):
    numStr = str(num)

    if len(numStr) % 2 != 0:
        return False

    mid = math.floor(len(numStr) / 2)

    if numStr[:mid] == numStr[mid:]:
        return True

    return False


def is_invalid_v2(num):
    n = str(num)
    size = len(n)
    acc = n[0]
    left = 1
    while len(acc) <= size // 2:
        rest = size - len(acc)
        if acc * ((rest // len(acc)) + 1) == n:
            return True
        else:
            acc += n[left]
            left += 1
    return False


def main():
    text = read_to_string("./input.txt")
    intervals = text.split(",")
    total = 0

    log = "interval: "

    for interval in intervals:
        log += interval
        start = int(interval.split("-")[0])
        stop = int(interval.split("-")[1])
        for num in range(start, stop + 1):
            if is_invalid_v2(num):
                log += " | invalid: " + str(num)
                total += num
            else:
                log += " | valid: " + str(num)
        log += "\n"

    # print(log)
    print("res: " + str(total))


main()
