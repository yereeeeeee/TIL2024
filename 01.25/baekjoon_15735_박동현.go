package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() int {
	bs.Scan()
	n, _ := strconv.Atoi(bs.Text())
	return n
}

func main() {
	defer bw.Flush()

	N := input()

	DP := make([]int, N+1)
	ans := 0
	for i := 1; i <= N; i++ {
		DP[i] = DP[i-1] + i
		ans += DP[i]
	}

	for i := N - 1; i > 0; i -= 2 {
		ans += DP[i]
	}

	bw.WriteString(strconv.Itoa(ans))
}
