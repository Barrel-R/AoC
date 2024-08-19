# --- part 1 ---


def findNumberLen(numbersDict, numIndex):
    if not numbersDict or numIndex not in numbersDict.keys():
        return 0

    lIndex = numIndex - 1
    rIndex = numIndex + 1
    len = 1

    for i, num in numbersDict.items():
        if i == numIndex:
            continue
        elif i == lIndex:
            len += 1
            lIndex -= 1
        elif i == rIndex:
            len += 1
            rIndex += 1
        else:
            return len

    return len


def parseLine(previousLine, line, nextLine):
    numbers = {}
    symbols = ["!", "@", "#", "$", "%", "&", "*",
               "(", ")", "-", "+", "=", "[", "]", "{", "}", ",", ";",
               "/", "|"]

    for i, char in enumerate(line):
        if char.isnumeric():
            numbers[i] = char

    print(line, findNumberLen(numbers, 0))
    # print(numbers)


def getValidParts(inputData):
    total = 0

    splitData = inputData.split('\n')

    for i, line in enumerate(splitData):
        previousLine = splitData[i - 1]

        if i == 0:
            previousLine = ""

        nextLine = ""

        if i + 1 < len(splitData) - 1:
            nextLine = splitData[i + 1]

        if line == "":
            break

        parseLine(previousLine, line, nextLine)

    return total


def main():
    with open('./sample_input.txt') as file:
        inputData = file.read()

    res = getValidParts(inputData)

    print(res)


main()
