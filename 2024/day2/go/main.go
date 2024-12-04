package main

import (
	"errors"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func setMode(cur, prev int, mode *string) {
	if cur > prev {
		*mode = "asc"
	} else {
		*mode = "desc"
	}
}

func handleMode(cur, prev int, mode *string) error {
	if len(*mode) == 0 {
		setMode(cur, prev, mode)
		return nil
	}

	if *mode == "asc" && cur <= prev {
		return errors.New("Break of mode found.")
	}

	if *mode == "desc" && cur >= prev {
		return errors.New("Break of mode found.")
	}

	return nil
}

func checkReport(report string) int {
	if len(report) == 0 {
		return 0
	}

	var mode string
	var distances []int

	nums := strings.Fields(report)

	for i, n := range nums {
		if i == 0 {
			continue
		}

		num, _ := strconv.Atoi(n)
		prevNum, _ := strconv.Atoi(nums[i-1])

		err := handleMode(num, prevNum, &mode)

		if err != nil {
			return 0
		}

		distance := int(math.Abs(float64(prevNum) - float64(num)))
		distances = append(distances, distance)
	}

	for _, n := range distances {
		if n > 3 || n < 1 {
			return 0
		}
	}

	return 1
}

func checkReportWithDampener(report string) int {
	if len(report) == 0 {
		return 0
	}

	var mode string
	var errIdxs []int

	nums := strings.Fields(report)
	var intNums []int

	for _, n := range nums {
		number, _ := strconv.Atoi(n)
		intNums = append(intNums, number)
	}

	for i, num := range intNums {
		if i == 0 {
			if nums[1] > nums[0] {
				mode = "asc"
			} else {
				mode = "desc"
			}

			continue
		}

		prevNum, _ := strconv.Atoi(nums[i-1])
		prevI := i - 1

		err := handleMode(num, prevNum, &mode)

		dist := int(math.Abs(float64(prevNum) - float64(num)))

		if err != nil || (dist > 3 || dist < 1) {
			errIdxs = append(errIdxs, prevI, i)

			if i < len(nums)-1 {
				errIdxs = append(errIdxs, i+1)
			}

		}
	}

	for _, idx := range errIdxs {
		newReport := removeLevel(nums, idx)

		if checkReport(strings.Join(newReport, " ")) == 1 {
			return 1
		}
	}

	if len(errIdxs) > 0 {
		return 0
	}

	return 1
}

func megaBruteForce(report string) int {
	if len(report) == 0 {
		return 0
	}

	nums := strings.Fields(report)

	for i := range nums {
		newReport := removeLevel(nums, i)
		if checkReport(strings.Join(newReport, " ")) == 1 {
			return 1
		}
	}

	return 0
}

func removeLevel(nums []string, index int) []string {
	ret := make([]string, 0)
	ret = append(ret, nums[:index]...)
	return append(ret, nums[index+1:]...)
}

func removeLevelV2(nums []int, index int) []int {
	ret := make([]int, 0)
	ret = append(ret, nums[:index]...)
	return append(ret, nums[index+1:]...)
}

func getSafeReports(data string) int {
	safeCount := 0
	unsafeCount := 0

	lines := strings.Split(data, "\n")

	for _, report := range lines {
		// safeCount += checkReport(report) // part 1
		// res := checkReportWithDampener(report) // part 2
		res := megaBruteForce(report)
		safeCount += res

		if res == 1 {
			fmt.Printf("report: %v, Safe, count: %v\n", report, safeCount)
		} else {
			unsafeCount += 1
			fmt.Printf("report: %v, Unsafe\n", report)
		}
	}

	return safeCount
}

func main() {
	data, err := os.ReadFile("./input.txt")

	if err != nil {
		fmt.Printf("error while reading the input file: %v\n", err)
	}

	sum := getSafeReports(string(data))

	fmt.Printf("sum: %v\n", sum)
}
