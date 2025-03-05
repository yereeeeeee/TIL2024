package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	ans = 1000
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func backtrack(idx, t int, arr []int) {
	ans = min(ans, abs(t))
	for i := idx + 1; i < len(arr); i++ {
		backtrack(i, t-arr[i], arr)
	}
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	arr := make([]int, N)
	total := 0
	for i := range arr {
		for j := range arr {
			num := input()
			arr[i] += num
			arr[j] += num
			total += num
		}
	}

	backtrack(0, total, arr)

	bw.WriteString(strconv.Itoa(ans))
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
