package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, E := input(), input()
	arr := make([]int, N)
	for i := 0; i < N; i++ {
		arr[i] = input()
	}
	sort.Ints(arr)
	now := arr[0]
	ans := 1
	for i := 1; i < N; i++ {
		if arr[i] >= now+E {
			ans++
		}
		now = arr[i]
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
