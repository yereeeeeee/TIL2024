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

	N, K := input(), input()

	DP := make([]int, K+1)
	for i := 0; i < N; i++ {
		score, time := input(), input()
		for j := K; j >= 0; j-- {
			if j+score <= K {
				DP[j+score] = max(DP[j+score], DP[j]+time)
			}
		}
	}
	fmt.Println(strconv.Itoa(DP[K]))
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
