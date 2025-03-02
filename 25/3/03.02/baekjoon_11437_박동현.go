package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

var (
	visit  []bool
	parent [][]int
	depth  []int
	graph  [][]int
	LOG    int
)

func dfs(now, d int) {
	depth[now] = d
	visit[now] = true

	for _, next := range graph[now] {
		if visit[next] {
			continue
		}
		parent[next][0] = now
		dfs(next, d+1)
	}
}

func buildSparseTable(N int) {
	for j := 1; j < LOG; j++ {
		for i := 1; i < N+1; i++ {
			if parent[i][j-1] > 0 {
				parent[i][j] = parent[parent[i][j-1]][j-1]
			}
		}
	}
}

func lca(a, b int) int {
	if depth[a] < depth[b] {
		a, b = b, a
	}

	diff := depth[a] - depth[b]
	for i := 0; i < LOG; i++ {
		if diff&(1<<i) > 0 {
			a = parent[a][i]
		}
	}

	if a == b {
		return a
	}

	for i := LOG - 1; i > -1; i-- {
		if parent[a][i] != parent[b][i] {
			a = parent[a][i]
			b = parent[b][i]
		}
	}
	return parent[a][0]
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	graph = make([][]int, N+1)
	for i := 0; i < N+1; i++ {
		graph[i] = make([]int, 0)
	}
	for i := 0; i < N-1; i++ {
		a, b := input(), input()
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}

	LOG = int(math.Ceil(math.Log2(float64(N))))

	visit = make([]bool, N+1)
	for i := 0; i < N+1; i++ {
		visit[i] = false
	}

	parent = make([][]int, N+1)
	for i := 0; i < N+1; i++ {
		parent[i] = make([]int, LOG)
	}
	depth = make([]int, N+1)

	dfs(1, 0)
	buildSparseTable(N)
	M := input()
	for i := 0; i < M; i++ {
		a, b := input(), input()
		bw.WriteString(fmt.Sprintln(lca(a, b)))
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
