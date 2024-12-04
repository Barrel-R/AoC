package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

// first line: seeds
// pipeline of calculating a + c , b + c and piping to next map
// calculation: number -> sourceRange + range length <= number ? destRange + number - sourceRange : number
// end of calculation: empty line
// new map: line ends with 'map:'

func parseSource(number int, line string) int {
	if len(line) == 0 || strings.Contains(line, "map") {
		return 0
	}

	numbers := strings.Split(line, " ")

	destRange, err := strconv.Atoi(numbers[0])

	if err != nil {
		fmt.Printf("error while converting str: %v\n", err)
		return 0
	}

	sourceRange, err := strconv.Atoi(numbers[1])

	if err != nil {
		fmt.Printf("error while converting str: %v\n", err)
		return 0
	}

	rangeLength, err := strconv.Atoi(numbers[2])

	if err != nil {
		fmt.Printf("error while converting str: %v\n", err)
		return 0
	}

	if sourceRange <= number && sourceRange+rangeLength > number {
		return number - sourceRange + destRange
	}

	return number
}

func getLowestLocation(locations []int) int {
	return slices.Min(locations)
}

func parseLines(seeds []int, lines []string) []int {
	locations := []int{}

	for _, seed := range seeds {
		number := seed
		for _, line := range lines {
			if len(line) > 0 {
				if strings.Contains(line, "map:") {
				}
				res := parseSource(number, line)

				if res > 0 {
					fmt.Printf("res: %v, line: %v\n", res, line)
					number = res
				}
			}
		}

		if number > 0 {
			locations = append(locations, number)
		}
	}

	return locations
}

func main() {
	data, err := os.ReadFile("./sample_input.txt")

	if err != nil {
		fmt.Printf("error while reading the input file: %v\n", err)
	}

	lines := strings.Split(string(data), "\n")
	seedsStr := strings.Split(lines[0], "seeds: ")[1]
	seeds := []int{}

	for _, seed := range strings.Fields(seedsStr) {
		seedNum, err := strconv.Atoi(seed)

		if err != nil {
			fmt.Printf("error while converting seed: %v\n", err)
		}

		seeds = append(seeds, seedNum)
	}

	locations := parseLines(seeds, lines[1:])

	fmt.Printf("locations: %v\n", locations)
	fmt.Printf("lowest: %v\n", getLowestLocation(locations))
}
