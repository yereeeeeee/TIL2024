package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const MAX_VALUE = math.MaxInt32

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := input(), input()
	banned := make(map[int]bool)
	for i := 0; i < M; i++ {
		banned[input()] = true
	}
	DP := make([][]int, N+1)
	for i := 0; i < N+1; i++ {
		DP[i] = make([]int, int(math.Sqrt(float64(2*N)))+2)
		for j := 0; j < len(DP[i]); j++ {
			DP[i][j] = MAX_VALUE
		}
	}
	DP[1][0] = 0

	for i := 2; i < N+1; i++ {
		if _, exists := banned[i]; exists {
			continue
		}
		for j := 1; j < int(math.Sqrt(float64(2*i))+1); j++ {
			DP[i][j] = min(DP[i-j][j-1], DP[i-j][j], DP[i-j][j+1]) + 1
		}
	}
	ans := MAX_VALUE
	for _, x := range DP[N] {
		ans = min(ans, x)
	}

	if ans == MAX_VALUE {
		ans = -1
	}
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
