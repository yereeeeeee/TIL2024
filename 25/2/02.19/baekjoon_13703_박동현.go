package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	K, N := input(), input()
	if K == 0 {
		bw.WriteString("0")
		return
	}

	DP := make([][]int64, N+1)
	for i := 0; i < N+1; i++ {
		DP[i] = make([]int64, K+N+1)
	}
	DP[0][K] = 1
	for i := 0; i < N; i++ {
		for j := 1; j < K+N; j++ {
			if DP[i][j] > 0 {
				DP[i+1][j+1] += DP[i][j]
				DP[i+1][j-1] += DP[i][j]
			}
		}
	}

	var ans int64
	ans = 0
	for i := 1; i < K+N+1; i++ {
		ans += DP[N][i]
	}

	bw.WriteString(fmt.Sprintln(ans))
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
