package main

import (
	"bufio"
	"fmt"
	"os"
)

const MAX_VALUE = 2500

func main() {
	defer bw.Flush()
	S := input()
	N := len(S)
	DP := make([]int, N+1)
	for i := 0; i < N+1; i++ {
		DP[i] = MAX_VALUE
	}
	for i := 0; i < 2*N-1; i++ {
		start, end := i/2, (i+1)/2
		for start >= 0 && end < N && S[start] == S[end] {
			start--
			if start < 0 {
				DP[end] = min(DP[end], 1)
			} else {
				DP[end] = min(DP[end], DP[start]+1)
			}
			end++
		}
	}
	bw.WriteString(fmt.Sprintln(DP[N-1]))
}

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() string {
	bs.Scan()
	return bs.Text()
}
