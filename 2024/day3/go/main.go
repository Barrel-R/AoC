package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func applyMul(matches []string) int {
	regex, err := regexp.Compile(`[0-9]+,[0-9]+`)

	if err != nil {
		fmt.Printf("error while compiling regex: %v\n", err)
	}

	sum := 0

	for _, match := range matches {
		nums := regex.FindString(match)
		splitNums := strings.Split(nums, ",")
		firstNum, _ := strconv.Atoi(splitNums[0])
		secNum, _ := strconv.Atoi(splitNums[1])
		sum += firstNum * secNum
	}

	return sum
}

func parseData(data string) {
	regex, err := regexp.Compile(`mul\([0-9]+,[0-9]+\)`)

	if err != nil {
		fmt.Printf("error while compiling regex: %v\n", err)
	}

	sum := 0

	matches := regex.FindAllString(data, -1)
	sum += applyMul(matches)

	fmt.Printf("sum: %v\n", sum)
}

func parseDataV2(data string) {
	regex, err := regexp.Compile(`mul\([0-9]+,[0-9]+\)`)

	if err != nil {
		fmt.Printf("error while compiling regex: %v\n", err)
	}

	matches := regex.FindAllStringIndex(data, -1)
	sum := parseWithCondition(data, matches)

	fmt.Printf("sum: %v\n", sum)
}

func parseWithCondition(data string, matchesIndex [][]int) int {
	enableCond, err := regexp.Compile(`do\(\)`)

	if err != nil {
		fmt.Printf("error while compiling regex: %v\n", err)
	}

	disableCond, err := regexp.Compile(`don't\(\)`)

	if err != nil {
		fmt.Printf("error while compiling regex: %v\n", err)
	}

	var matches []string

	// fmt.Printf("matchesI: %v\n", matchesIndex)

	enables := enableCond.FindAllStringIndex(data, -1)
	disables := disableCond.FindAllStringIndex(data, -1)
	// fmt.Printf("enables: %v, disables: %v\n", enables, disables)

	for _, indexes := range matchesIndex {
		match := data[indexes[0]:indexes[1]]
		var lastEnable int
		var lastDisable int

		for _, disIdxs := range disables {
			if disIdxs[1] <= indexes[0] {
				lastDisable = disIdxs[1]
			} else {
				break
			}
		}

		for _, enIdxs := range enables {
			if enIdxs[1] <= indexes[0] {
				lastEnable = enIdxs[1]
			} else {
				break
			}
		}

		// fmt.Printf("last enable: %v, last disable: %v\n", lastEnable, lastDisable)

		if len(disables) == 0 || lastDisable == 0 || lastEnable > lastDisable {
			matches = append(matches, match)
			// fmt.Printf("appending: %v, idx: %v\n", match, indexes[0])
		}
	}

	return applyMul(matches)
}

func main() {
	data, err := os.ReadFile("./input.txt")

	if err != nil {
		fmt.Printf("couldn't read the file: %v\n", err)
	}

	parseDataV2(string(data))
}
