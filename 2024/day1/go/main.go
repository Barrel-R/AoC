package main

import (
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

func getArrays(data string) ([]int, []int) {
	lines := strings.Split(data, "\n")
	var first []int
	var sec []int

	for _, line := range lines {
		nums := strings.Fields(line)

		if len(nums) < 2 {
			continue
		}

		firstNum, _ := strconv.Atoi(nums[0])
		secNum, _ := strconv.Atoi(nums[1])

		first = append(first, firstNum)
		sec = append(sec, secNum)
	}

	// fmt.Printf("first: %v\n", first)
	// fmt.Printf("sec: %v\n", sec)

	return first, sec
}

func parseArrays(first, sec []int) int {
	var sum = 0

	slices.Sort(first)
	slices.Sort(sec)

	for i := range len(first) {
		distance := math.Abs(float64(first[i]) - float64(sec[i]))
		sum += int(distance)
	}

	return sum
}

func getSimilarities(first, sec []int) int {
	var similarities int
	numCount := make(map[int]int)

	for _, num := range sec {
		numCount[num] += 1
	}

	for _, num := range first {
		similarities += num * numCount[num]
	}

	return similarities
}

func main() {
	data, err := os.ReadFile("./input.txt")

	if err != nil {
		fmt.Printf("error while reading the input file: %v\n", err)
	}

	sum := 0

	first, sec := getArrays(string(data))

	sum += getSimilarities(first, sec)

	fmt.Printf("sum: %v\n", sum)
}
