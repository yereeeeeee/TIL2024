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

	tc := input()
	for t := 0; t < tc; t++ {

		N := input()
		coins := make([]int, N)
		for i := 0; i < N; i++ {
			coins[i] = input()
		}
		M := input()
		DP := make([]int, M+1)
		DP[0] = 1
		for _, coin := range coins {
			for i := coin; i <= M; i++ {
				DP[i] += DP[i-coin]
			}
		}
		bw.WriteString(fmt.Sprintln(DP[M]))
	}
}

// fastIO
var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() int {
	bs.Scan()
	num, _ := strconv.Atoi(bs.Text())
	return num
}
