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

sampleInputV3 = """eightoneeight
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
sevennine7eightpmlxqprzvjone
oneight"""

writtenNumbers = ["one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine"]


def checkWord(word):
    return word in writtenNumbers


def formWord(word, nextLetter):
    if word == "":
        return nextLetter

    res = any(w.startswith(word + nextLetter) for w in writtenNumbers)

    if res:
        return word + nextLetter
    else:
        return formWord(word[1::], nextLetter)


def getNumbers(line, numbers, words):
    if len(words) == 0:
        return numbers[0] + numbers[-1]

    if len(numbers) == 0:
        return str(writtenNumbers[words[0]]) + str(writtenNumbers[words[-1]])

    firstNumIndex = line.find(numbers[0])
    firstWordIndex = line.find(words[0])

    lastNumIndex = line.rindex(numbers[-1])
    lastWordIndex = line.rindex(words[-1])

    firstRes = ""
    lastRes = ""

    if firstNumIndex < firstWordIndex:
        firstRes = numbers[0]
    else:
        firstRes = str(writtenNumbers.index(words[0]) + 1)

    if lastNumIndex > lastWordIndex:
        lastRes = numbers[-1]
    else:
        lastRes = str(writtenNumbers.index(words[-1]) + 1)

    return firstRes + lastRes


def parseLineV2(line):
    if line == "":
        return 0

    numbers = []
    formingWord = ""
    words = []

    for n in range(len(line)):
        if checkWord(formingWord):
            words.append(formingWord)

        if line[n].isdigit():
            numbers.append(line[n])
        if line[n].isalpha():
            formingWord = formWord(formingWord, line[n])
            if checkWord(formingWord):
                words.append(formingWord)

    res = getNumbers(line, numbers, words)

    return res


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

    res = sumParsedLines(inputData)

    print(res)


main()
