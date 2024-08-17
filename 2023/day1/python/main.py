sampleInput = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

sampleInputV2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

fuck = """eightoneeight
two9hjfsdfnone3jsdf29
fmbbkfsdlknajxzclk24eight7
seightq45qonee
ztwonez
xoneeight
sevenine
sevenicn
twooneight
seightq45qonee
fmbbkfsdlknajxzclk24eight7
two9hjfsdfnone3jsdf29
eightwo5
eightwo
one
47xkjdlcnvxpfddz
oneight"""

what = "47xkjdlcnvxpfddz"

sampleInputV3 = "sevennine7eightpmlxqprzvjone"


def parseLineV2(line):
    if line == "":
        return 0

    left = 0
    right = len(line) - 1
    leftNum = ""
    rightNum = ""
    formingWordLeft = ""
    formingWordRight = ""

    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
               "seven": 7, "eight": 8, "nine": 9}

    reversedKeys = [i[::-1] for i in numbers.keys()]

    while left < len(line):
        if leftNum == "":
            if line[left].isdigit():
                if formingWordLeft in numbers.keys():
                    leftNum = str(numbers[formingWordLeft])
                    continue

                leftNum = line[left]
            if line[left].isalpha():
                if formingWordLeft in numbers.keys():
                    leftNum = str(numbers[formingWordLeft])

                res = any(w.startswith(formingWordLeft)
                          for w in numbers.keys())

                print('l', formingWordLeft, res)

                if res:
                    if formingWordLeft in numbers.keys():
                        leftNum = str(numbers[formingWordLeft])
                    else:
                        formingWordLeft += line[left]
                        if formingWordLeft in numbers.keys():
                            leftNum = str(numbers[formingWordLeft])
                else:
                    if not formingWordLeft == "":
                        left -= 1
                        formingWordLeft = formingWordLeft[1::]

        if rightNum == "":
            if line[right].isdigit():
                if formingWordRight in reversedKeys:
                    rightNum = str(numbers[formingWordRight[::-1]])
                    continue

                rightNum = line[right]
            if line[right].isalpha():
                if formingWordRight in reversedKeys:
                    rightNum = str(numbers[formingWordRight[::-1]])

                res = any(w.startswith(
                    formingWordRight) for w in reversedKeys)

                print('r', formingWordRight, res)

                if res:
                    if formingWordRight in reversedKeys:
                        rightNum = str(numbers[formingWordRight[::-1]])
                    else:
                        formingWordRight += line[right]
                        if formingWordRight in reversedKeys:
                            rightNum = str(numbers[formingWordRight[::-1]])
                else:
                    if not formingWordRight == "":
                        right += 1
                        formingWordRight = formingWordRight[1::]

        left += 1
        right -= 1

    print(line, leftNum or rightNum, rightNum or leftNum)

    return (leftNum or rightNum) + (rightNum or leftNum)  # concat strings


def parseLine(line):
    if line == "":
        return 0

    left = 0
    right = len(line) - 1
    leftNum = ""
    rightNum = ""

    while left < right or leftNum == "" or rightNum == "":
        if leftNum == "" and line[left].isdigit():
            leftNum = line[left]

        if rightNum == "" and line[right].isdigit():
            rightNum = line[right]

        left += 1
        right -= 1

    return leftNum + rightNum  # concat strings


def sumParsedLines(input):
    total = 0
    lines = input.split("\n")

    for line in lines:
        total += int(parseLineV2(line))

    return total


def main():
    with open("./input.txt") as file:
        inputData = file.read()

    res = sumParsedLines(what)

    print(res)


main()
