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

	N, K, M := input(), input(), input()

	queue := make([]int, N)
	for i := 0; i < N; i++ {
		queue[i] = i + 1
	}

	idx := 0
	cw := true
	for len(queue) > 0 {
		if cw {
			idx = (idx + K - 1) % len(queue)
		} else {
			idx = (idx - (K % len(queue)) + len(queue)) % len(queue)
		}
		bw.WriteString(fmt.Sprintln(queue[idx]))
		queue = append(queue[:idx], queue[idx+1:]...)

		if len(queue) > 0 && (N-len(queue))%M == 0 {
			cw = !cw
		}
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
