package main

import (
	"bufio"
	"os"
	"slices"
	"strconv"
)

var (
	dx = [4]int{0, 1, 0, -1}
	dy = [4]int{1, 0, -1, 0}
)

func fillArr(arr *[][]int, size int) {
	for i := 0; i < len(*arr); i++ {
		(*arr)[i] = make([]int, size)
		for j := 0; j < size; j++ {
			(*arr)[i][j] = input()
		}
	}
}

func isEqual(arr, brr [][]int) bool {
	for i := 0; i < len(arr); i++ {
		if !slices.Equal(arr[i], brr[i]) {
			return false
		}
	}
	return true
}

func dfs(N, M, x, y, now, nxt int, arr *[][]int) {
	if (*arr)[x][y] != now {
		return
	}
	(*arr)[x][y] = nxt

	for i := 0; i < 4; i++ {
		nx, ny := x+dx[i], y+dy[i]
		if 0 <= nx && nx < N && 0 <= ny && ny < M {
			dfs(N, M, nx, ny, now, nxt, arr)
		}
	}
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := input(), input()
	before := make([][]int, N)
	fillArr(&before, M)
	after := make([][]int, N)
	fillArr(&after, M)
	cnt := 0
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			if before[i][j] != after[i][j] {
				dfs(N, M, i, j, before[i][j], after[i][j], &before)
				cnt++
				if cnt > 1 {
					bw.WriteString("NO")
					return
				}
			}
		}
	}
	if isEqual(before, after) {
		bw.WriteString("YES")
	} else {
		bw.WriteString("NO")
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
