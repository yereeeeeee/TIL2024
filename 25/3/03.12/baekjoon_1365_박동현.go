package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func bis(x int, arr []int) int {
	start, end := 0, len(arr)-1

	for start <= end {
		mid := (start + end) / 2
		if arr[mid] == x {
			return mid
		} else if arr[mid] < x {
			start = mid + 1
		} else {
			end = mid - 1
		}
	}
	return start
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = input()
	}

	DP := make([]int, 0)
	DP = append(DP, arr[0])

	for _, x := range arr {
		if DP[len(DP)-1] < x {
			DP = append(DP, x)
		} else {
			DP[bis(x, DP)] = x
		}
	}
	bw.WriteString(fmt.Sprintln(N - len(DP)))
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() int {
	bs.Scan()
	num, _ := strconv.Atoi(bs.Text())
	return num
}
