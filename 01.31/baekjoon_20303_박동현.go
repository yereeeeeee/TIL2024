package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	bs     = bufio.NewScanner(os.Stdin)
	bw     = bufio.NewWriter(os.Stdout)
	parent []int
	cnt    []int
	arr    []int
)

// union - find
func find(x int) int {
	if parent[x] != x {
		parent[x] = find(parent[x])
	}
	return parent[x]
}

func union(x, y int) {
	rootX := find(x)
	rootY := find(y)
	if rootX == rootY {
		return
	}

	if rootX > rootY {
		rootX, rootY = rootY, rootX
	}
	parent[rootY] = rootX
	arr[rootX] += arr[rootY]
	cnt[rootX] += cnt[rootY]
}

// main
func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M, K := input(), input(), input()
	arr = make([]int, N+1)
	for i := 1; i <= N; i++ {
		arr[i] = input()
	}

	parent = make([]int, N+1)
	cnt = make([]int, N+1)
	for i := 1; i <= N; i++ {
		cnt[i] = 1
		parent[i] = i
	}

	for i := 0; i < M; i++ {
		a, b := input(), input()
		union(a, b)
	}

	DP := make([]int, K)
	for i := 1; i <= N; i++ {
		if i == parent[i] {
			child := cnt[i]
			candies := arr[i]
			for j := K - 1; j > child-1; j-- {
				DP[j] = max(DP[j], DP[j-child]+candies)
			}
		}
	}
	bw.WriteString(strconv.Itoa(DP[K-1]))
}

// fastIO
func input() int {
	bs.Scan()
	num, _ := strconv.Atoi(bs.Text())
	return num
}
