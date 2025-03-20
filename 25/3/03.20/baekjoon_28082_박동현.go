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
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = input()
	}

	length := 50001
	DP := make([]int, length)
	for i := 1; i < length; i++ {
		DP[i] = K + 1
	}

	for _, v := range arr {
		for i := length - v - 1; i >= 0; i-- {
			DP[i+v] = min(DP[i+v], DP[i]+1)
		}
	}

	ans := make([]int, 0)
	for i := 1; i < length; i++ {
		if DP[i] <= K {
			ans = append(ans, i)
		}
	}
	bw.WriteString(fmt.Sprintln(len(ans)))
	for i := 0; i < len(ans); i++ {
		bw.WriteString(fmt.Sprintf("%d ", ans[i]))
	}
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
