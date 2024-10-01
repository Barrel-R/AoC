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
    line = "." + splitData[lineIndex] + "."

    for i, char in enumerate(line):
        prevIndex = i - len(mountingNum) - 1
        if char.isnumeric():
            mountingNum += char
        elif char in symbols or (line[prevIndex] in symbols and mountingNum != ""):
            validNumbers.append(mountingNum)
            mountingNum = ""
        elif mountingNum != "":
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
    borderLines = "." * (len(splitData[0])) + "\n"
    actualData = borderLines + inputData + borderLines

    validNumbers = []

    for i in range(len(splitData)):
        validNumbers += getValidNumbers(actualData.split("\n"), i)

    print(validNumbers)

    res = sum([int(n) for n in filter(lambda x: x != "",  validNumbers)])

    print(res)


main()
