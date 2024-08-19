# utils

def getNumAndColor(gameSet):
    cubes = [x.strip() for x in gameSet.split(',')]

    for cube in cubes:
        values = cube.split(' ')
        num = int(values[0])
        color = values[1]

    return (num, color)


def getLineSets(line):
    startingIndex = line.find(':') + 2
    return [x.strip() for x in line[startingIndex:].split(';')]


# --- PART 1 ---


def validateSet(gameSet):
    if gameSet == "":
        return False

    totalLookup = {"red": 12, "green": 13, "blue": 14}

    (num, color) = getNumAndColor(gameSet)

    if totalLookup[color] < num:
        return False

    return True


def parseLine(line):
    if line == "":
        return 0

    id = line.split(':')[0].split('Game ')[1]

    for gameSet in getLineSets(line):
        if not validateSet(gameSet):
            return 0

    return int(id)


def sumIds(data):
    total = 0

    for line in data.split('\n'):
        total += parseLine(line)

    return total


def main():
    with open("./input.txt") as file:
        inputData = file.read()

    part1_res = sumIds(inputData)
    part2_res = getPowersSum(inputData)

    print(part1_res)
    print(part2_res)


# --- PART 2 ---


def getPower(line):
    if line == "":
        return 0

    minCubes = {"red": 0, "green": 0, "blue": 0}

    sets = getLineSets(line)

    for gameSet in sets:
        cubes = [x.strip() for x in gameSet.split(',')]

        for cube in cubes:
            values = cube.split(' ')
            num = int(values[0])
            color = values[1]

            if minCubes[color] < num:
                minCubes[color] = num

    return minCubes["red"] * minCubes["green"] * minCubes["blue"]


def getPowersSum(inputData):
    total = 0

    for line in inputData.split('\n'):
        total += getPower(line)

    return total


main()
