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

    while left < right or leftNum == "" or rightNum == "":
        if leftNum == "":
            if line[left].isdigit() and leftNum == "":
                leftNum = line[left]
            if line[left].isalpha() and leftNum == "":
                if formingWordLeft in numbers.keys():
                    leftNum = str(numbers[formingWordLeft])

                res = any(w.startswith(formingWordLeft)
                          for w in numbers.keys())

                if res:
                    formingWordLeft += line[left]
                else:
                    newIndex = left - len(formingWordLeft) - 1
                    formingWordLeft = line[newIndex]
                    left = newIndex

        if rightNum == "":
            if line[right].isdigit() and rightNum == "":
                rightNum = line[right]
            if line[left].isalpha() and rightNum == "":
                if formingWordRight in reversedKeys:
                    rightNum = str(numbers[formingWordRight[::-1]])
                res = any(w.startswith(formingWordRight) for w in reversedKeys)

                if res:
                    formingWordRight += line[right]
                else:
                    newIndex = right + len(formingWordRight) - 1
                    formingWordRight = line[newIndex]
                    right = newIndex

        left += 1
        right -= 1

    print(line, leftNum, rightNum)

    return leftNum + rightNum  # concat strings


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

    # total += int(parseLineV2("seigh1toneight"))

    for line in lines:
        total += int(parseLineV2(line))

    return total


def main():
    with open("./input.txt") as file:
        inputData = file.read()

    res = sumParsedLines(inputData)

    print(res)


main()
