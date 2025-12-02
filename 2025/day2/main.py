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


def first_part(text):
    intervals = text.split(",")
    total = 0

    for interval in intervals:
        start = int(interval.split("-")[0])
        stop = int(interval.split("-")[1])
        for num in range(start, stop + 1):
            if is_invalid(num):
                total += num

    return total


def main():
    text = read_to_string("./input.txt")
    res = first_part(text)

    print("res: " + str(res))


main()
