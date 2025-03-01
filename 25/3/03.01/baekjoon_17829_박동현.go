package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func dnc(x, y, size int, arr [][]int) int {
	if size == 1 {
		return arr[x][y]
	}
	res := make([]int, 4)
	idx := [2]int{0, size / 2}
	for n, i := range idx {
		for m, j := range idx {
			res[2*n+m] = dnc(x+i, y+j, size/2, arr)
		}
	}
	sort.Ints(res)

	return res[2]
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()

	arr := make([][]int, N)
	for i := 0; i < N; i++ {
		arr[i] = make([]int, N)
		for j := 0; j < N; j++ {
			arr[i][j] = input()
		}
	}
	bw.WriteString(fmt.Sprintln(dnc(0, 0, N, arr)))
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
