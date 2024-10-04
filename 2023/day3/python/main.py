# --- part 1 ---
symbols = ["!", "@", "#", "$", "%", "&", "*",
           "(", ")", "-", "+", "=", "[", "]", "{", "}", ",", ";",
           "/", "|"]


def checkLine(numbersToCheck, previousLine, nextLine):
    validNumbers = []

    for indexTuple in numbersToCheck:
        if any(char in symbols for char in previousLine[indexTuple[0]:indexTuple[1] + 1]):
            validNumbers.append(indexTuple[2])
        elif any(char in symbols for char in nextLine[indexTuple[0]:indexTuple[1] + 1]):
            validNumbers.append(indexTuple[2])

    return validNumbers


def getValidNumbers(splitData, lineIndex):
    validNumbers = []
    numbersToCheck = []
    mountingNum = ""
    line = "." + splitData[lineIndex] + "."  # facilitate boundary checking

    for i, char in enumerate(line):
        prevIndex = i - len(mountingNum) - 1
        if char.isnumeric():
            mountingNum += char
        # check char and previous for symbols
        elif char in symbols or (line[prevIndex] in symbols and mountingNum != ""):
            validNumbers.append(mountingNum)
            mountingNum = ""
        elif mountingNum != "":
            # create tuple with range of indexes to check in previous and next lines
            numbersToCheck.append(
                (max(0, prevIndex), min(i, len(line)), mountingNum))
            mountingNum = ""

    previousLine = ""
    nextLine = ""

    if lineIndex > 0:
        previousLine = "." + splitData[lineIndex - 1] + "."

    if lineIndex < len(splitData) - 1:
        nextLine = "." + splitData[lineIndex + 1] + "."

    validNumbers += checkLine(numbersToCheck, previousLine, nextLine)

    return validNumbers


def main():
    with open('./input.txt') as file:
        inputData = file.read()

    splitData = inputData.split("\n")
    # facilitate boundary checking
    borderLines = "." * (len(splitData[0])) + "\n"
    actualData = borderLines + inputData + borderLines

    validNumbers = []

    # actually use splitData len so index does not go out of range
    for i in range(len(splitData)):
        validNumbers += getValidNumbers(actualData.split("\n"), i)

    res = sum([int(n) for n in filter(lambda x: x != "",  validNumbers)])

    print(res)


# main()


# --- part 2 ---

"""
Description:

A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.

What is the sum of all of the gear ratios in your engine schematic?

maximum adjacent numbers = 6
length of line is always the same

add borders of . to line, vertically and horizontally

for i in lineRange:
    if line[i] == *:

        if previousLine:
            - check from i - 1 to i + 1 in previousLine for numbers
            - what if range has two separate numbers? (Ex: ['3', '.', '5'])
        if nextLine:
            - check from i - 1 to i + 1 in nextLine for numbers
            - what if range has two separate numbers? (Ex: ['3', '.', '5'])

        - check i - 1 in line for numbers
        - check i + 1 in line for numbers

        if number is found:
            - add it to str and keep going until char isn't a number
        if adjcent numbers len is 2:
            add to product of numbers to gears and nullify numbers

        next iteration

checking the line:
    consider i - 1 or i where i is the symbol index:
        if it is a number, we have to check backwards and reverse the string
        to get the full number
    for char in range:
        if char is numeric:
            add to num str
        else:
            add num str to arr and nullify num str
            next iteration
"""


def getNumbers(symbolIndex, line):
    numbers = []
    num = ""
    backwardsNum = ""
    forwardNum = ""
    maxLen = len(line) - 1
    indexRange = [max(0, symbolIndex - 1),
                  symbolIndex, min(symbolIndex + 1, maxLen)]

    if line[indexRange[0]].isnumeric():
        left = indexRange[0] - 1  # check backwards for num
        while line[left].isnumeric() and left >= 0:
            backwardsNum += line[left]
            left -= 1
        if line[left] == "-":
            backwardsNum += "-"
        num += backwardsNum[::-1] + line[indexRange[0]]

    if line[indexRange[1]].isnumeric():
        if line[indexRange[1] - 1] == "-":
            num += "-"
        num += line[indexRange[1]]
    elif num != "":
        numbers.append(int(num))
        num = ""

    if line[indexRange[2]].isnumeric():
        right = indexRange[2] + 1
        while line[right].isnumeric() and right <= maxLen:
            forwardNum += line[right]
            right += 1
        num += line[indexRange[2]] + forwardNum
        if line[indexRange[2] - 1] == "-":
            num = num * -1
        numbers.append(int(num))
    elif num != "":
        numbers.append(int(num))

    return numbers


def checkCurrentLine(symbolIndex, line):
    numbers = []
    left = max(0, symbolIndex - 1)
    right = min(symbolIndex + 1, len(line) - 1)
    leftNum = ""
    rightNum = ""

    while line[left].isnumeric() and left >= 0:
        leftNum += line[left]
        left -= 1

    while line[right].isnumeric() and right < len(line) - 1:
        rightNum += line[right]
        right += 1

    if leftNum != "":
        numbers.append(int(leftNum[::-1]))

    if rightNum != "":
        numbers.append(int(rightNum))

    return numbers


def getLineGears(splitData, lineIndex):
    gears = []
    symbol = "*"
    numbers = []
    debugNum = []
    line = "." + splitData[lineIndex] + "."
    previousLine = "." + splitData[lineIndex -
                                   1] + "." if lineIndex > 0 else ""

    nextLine = "." + splitData[lineIndex + 1] + \
        "." if lineIndex < len(splitData) - 1 else ""

    for i, char in enumerate(line):
        if char == symbol:
            if previousLine:
                numbers += getNumbers(i, previousLine)
            if nextLine:
                numbers += getNumbers(i, nextLine)

            currentLine = checkCurrentLine(i, line)

            if currentLine:
                numbers += currentLine

        if len(numbers) == 2:
            gears.append(numbers[0] * numbers[1])
            debugNum.append(numbers[0])
            debugNum.append(numbers[1])
        numbers = []

    return gears


def mainPart2():
    with open('./input.txt') as file:
        inputData = file.read()

    splitData = inputData.split("\n")
    borderLines = "." * (len(splitData[0])) + "\n"
    actualData = borderLines + inputData + borderLines

    gearSum = []

    for i in range(len(splitData)):
        gearSum += getLineGears(actualData.split("\n"), i)

    res = sum(gearSum)

    print('sum: ', res)


mainPart2()
