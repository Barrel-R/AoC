import math


def read_to_string(path):
    with open(path) as f:
        string = f.read()
        return string


def read_to_list(path):
    with open(path) as f:
        lines = f.read().splitlines()
        return lines


def first_part(lines):
    cur = 50
    res = 0

    for command in lines:
        dir = command[0]
        num = int(command[1:]) % 100

        if dir == "L":
            if cur - num < 0:
                cur = 100 - abs(cur - abs(num))
            else:
                cur -= num
        else:
            if cur + num > 99:
                cur = 0 + abs(100 - (cur + num))
            else:
                cur += num

        if cur == 0:
            res += 1

    return res


def second_part(lines):
    cur = 50
    res = 0

    for command in lines:
        dir = command[0]
        num = int(command[1:]) % 100
        res += math.floor(int(command[1:]) / 100)

        if dir == "L":
            if cur - num < 0:
                old = cur
                cur = 100 - abs(cur - abs(num))
                if cur != 0 and old != 0:
                    res += 1
            else:
                cur -= num
        else:
            if cur + num > 99:
                old = cur
                cur = 0 + abs(100 - (cur + num))
                if cur != 0 and old != 0:
                    res += 1
            else:
                cur += num

        if cur == 0:
            res += 1

    return res


def main():
    lines = read_to_list("./input.txt")
    res = second_part(lines)
    print("res: " + str(res))


main()
