package utils

import (
	"fmt"
	"os"
	"strings"
)

func parseLines(data []byte) []string {
	return strings.Split(string(data), "\n")
}

func getResult() {
	data, err := os.ReadFile("./input.txt")

	if err != nil {
		fmt.Printf("error while reading the input file: %v\n", err)
	}

	lines := parseLines(data)
}
