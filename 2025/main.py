def read_to_string(path):
    with open(path) as f:
        string = f.read()
        return string


def read_to_list(path):
    with open(path) as f:
        lines = f.read().splitlines()
        return lines


def first_day_first_part(lines):
    cur = 50
    res = 0

    for command in lines:
        dir = command[0]
        num = int(command[1:]) % 100

        log = "command: " + command + " | cur before: " + str(cur) + " | "

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

        log += "new cur: " + str(cur)

        print(log)

    return res


def first_day_second_part(lines):
    cur = 50
    res = 0

    for command in lines:
        dir = command[0]
        num = int(command[1:]) % 100

        log = "command: " + command + " | cur before: " + str(cur) + " | "

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

        log += "new cur: " + str(cur)

        print(log)

    return res


def main():
    lines = read_to_list("./sample.txt")
    res = first_day_first_part(lines)
    print("res: " + str(res))


main()
