package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func applyMul(matches []string) int {
	regex, _ := regexp.Compile(`[0-9]+,[0-9]+`)
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

func parseLines(lines []string) {
	regex, _ := regexp.Compile(`mul\([0-9]+,[0-9]+\)`)
	sum := 0

	for _, line := range lines {
		matches := regex.FindAllString(line, -1)
		fmt.Printf("matches: %v\n", matches)
		sum += applyMul(matches)
	}

	fmt.Printf("sum: %v\n", sum)
}

func main() {
	data, err := os.ReadFile("./input.txt")

	if err != nil {
		fmt.Printf("couldn't read the file: %v\n", err)
	}

	lines := strings.Split(string(data), "\n")

	parseLines(lines)
}
