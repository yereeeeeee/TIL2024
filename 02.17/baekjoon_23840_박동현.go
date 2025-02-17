package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

const MAX_VALUE = 1e12

var (
	N     int
	M     int
	K     int
	graph [][]Node
	DP    [][]int64
	arr   [][]int64
)

type Node struct {
	x    int
	cost int64
}

func (n Node) unpack() (int, int64) {
	return n.x, n.cost
}

type HeapQ []Node

func (h HeapQ) Len() int {
	return len(h)
}

func (h HeapQ) Less(i, j int) bool {
	return h[i].cost < h[j].cost
}

func (h HeapQ) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *HeapQ) Push(x interface{}) {
	*h = append(*h, x.(Node))
}

func (h *HeapQ) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func dijkstra(start int) []int64 {
	distance := make([]int64, N+1)
	for i := 0; i <= N; i++ {
		distance[i] = MAX_VALUE
	}
	hq := &HeapQ{}
	heap.Init(hq)
	hq.Push(Node{start, 0})
	distance[start] = 0
	for hq.Len() > 0 {
		now, distNow := heap.Pop(hq).(Node).unpack()

		if distNow > distance[now] {
			continue
		}

		for _, node := range graph[now] {
			nxt, cost := node.unpack()
			if distance[nxt] > distance[now]+cost {
				distance[nxt] = distance[now] + cost
				heap.Push(hq, Node{nxt, distance[nxt]})
			}
		}
	}
	return distance
}

func tsp(now, bit int) int64 {
	if bit == (1<<K)-1 {
		return arr[now][K+1]
	}

	if DP[now][bit] > -1 {
		return DP[now][bit]
	}

	DP[now][bit] = MAX_VALUE
	for nxt := 0; nxt < K; nxt++ {
		if bit&(1<<nxt) == 0 && arr[now][nxt] != MAX_VALUE {
			DP[now][bit] = min(DP[now][bit], tsp(nxt, bit|(1<<nxt))+arr[now][nxt])
		}
	}
	return DP[now][bit]
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M = input(), input()
	graph = make([][]Node, N+1)
	for i := 0; i <= N; i++ {
		graph[i] = make([]Node, 0)
	}
	for i := 0; i < M; i++ {
		a, b, c := input(), input(), input()
		cost := int64(c)
		graph[a] = append(graph[a], Node{b, cost})
		graph[b] = append(graph[b], Node{a, cost})
	}

	start, end := input(), input()

	K = input()

	toVisit := make([]int, K+2)

	for i := 0; i < K; i++ {
		toVisit[i] = input()
	}

	toVisit[K] = start
	toVisit[K+1] = end

	arr = make([][]int64, K+2)
	for i := 0; i < K+2; i++ {
		arr[i] = make([]int64, K+2)
	}

	for i := 0; i < K+2; i++ {
		distance := dijkstra(toVisit[i])
		for j := 0; j < K+2; j++ {
			arr[i][j] = distance[toVisit[j]]
		}
	}

	DP = make([][]int64, K+1)
	for i := 0; i < K+1; i++ {
		DP[i] = make([]int64, 1<<K)
		for j := 0; j < 1<<K; j++ {
			DP[i][j] = -1
		}
	}

	ans := tsp(K, 0)
	if ans >= MAX_VALUE {
		bw.WriteString("-1")
	} else {
		bw.WriteString(fmt.Sprint(ans))
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
