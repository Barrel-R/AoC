sampleInput = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


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
        total += int(parseLine(line))

    return total


def main():
    with open("./input.txt") as file:
        inputData = file.read()

    res = sumParsedLines(inputData)

    print(res)


main()
