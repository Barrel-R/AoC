package main

import (
	"fmt"
	"os"
	"strings"
)

func parseLines(lines []string) {
	sum := 0

	const keyword = "XMAS"
	const reversedKeyword = "SAMX"

	var stack []byte

	for i, line := range lines {
		for j, c := range line {
		}
	}

	fmt.Printf("sum: %v\n", sum)
}

func main() {
	data, err := os.ReadFile("./sample_input.txt")

	if err != nil {
		fmt.Printf("error while reading file: %v\n", err)
	}

	lines := strings.Split(string(data), "\n")

	parseLines(lines)
}
