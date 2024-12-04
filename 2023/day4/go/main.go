package main

import (
	"fmt"
	"maps"
	"os"
	"slices"
	"strconv"
	"strings"
)

// --- part 2 ---

func parseLineFast(lines []string) int {
	cardInstances := make([]int, len(lines))
	for i := range cardInstances {
		cardInstances[i] = 1
	}

	for i := 0; i < len(lines); i++ {
		matching := countMatchingNums(lines[i])
		for j := 1; j <= matching && i+j < len(lines); j++ {
			cardInstances[i+j] += cardInstances[i]
		}
	}

	sum := 0
	for _, instances := range cardInstances {
		sum += instances
	}
	return sum
}

var cardMap = make(map[int]int, 1000) // cardId: number_of_instances
var knownMatches = make(map[int]int, 1000)
var lines []string

func parseLineRec(startIndex int) {
	if startIndex > len(lines)-1 || lines[startIndex] == "" {
		return
	}

	split := strings.Split(strings.Split(lines[startIndex], ":")[0], " ")
	cardId := split[len(split)-1]
	idNum, err := strconv.Atoi(cardId)

	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}

	cardMap[idNum] += 1

	var matching int

	if knownMatches[startIndex] != 0 {
		matching = knownMatches[startIndex]
	} else {
		matching = countMatchingNums(lines[startIndex])
		knownMatches[startIndex] = matching
	}

	for n := 0; n < matching; n++ {
		parseLineRec(startIndex + n + 1)
	}

	return
}

func countMatchingNums(line string) int {
	var count int

	if len(line) == 0 {
		return count
	}

	numbers := strings.Split(line, "|")

	// first char is space so go from index 1 forward
	winNums := strings.Split(strings.Split(numbers[0], ":")[1], " ")[1:]
	myNums := strings.Split(numbers[1], " ")[1:]

	for _, num := range myNums {
		if slices.Contains(winNums, num) && num != "" {
			count += 1
		}
	}

	return count
}

// --- part 1 ---
func parseLine(line string) (int, error) {
	if len(line) == 0 {
		return 0, nil
	}

	numbers := strings.Split(line, "|")

	// first char is space so go from index 1 forward
	winNums := strings.Split(strings.Split(numbers[0], ":")[1], " ")[1:]
	myNums := strings.Split(numbers[1], " ")[1:]

	cardMult := 0

	for _, num := range myNums {
		if slices.Contains(winNums, num) && num != "" {
			if cardMult == 0 {
				cardMult = 1
			} else {
				cardMult = cardMult * 2
			}
		}
	}

	// fmt.Printf("card: %v, num: %v\n", line[:6], cardMult)

	return cardMult, nil
}

func main() {
	data, err := os.ReadFile("./input.txt")

	if err != nil {
		fmt.Printf("error while reading the input file: %v\n", err)
	}

	sum := 0

	ls := strings.Split(string(data), "\n")
	lines = ls

	fmt.Printf("fast: %v\n", parseLineFast(lines))

	for val := range maps.Values(cardMap) {
		sum += val
	}

	fmt.Printf("map: %v\n", cardMap)
	fmt.Printf("sum: %v\n", sum)
}
