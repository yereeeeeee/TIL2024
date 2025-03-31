package main

import (
	"bufio"
	"container/heap"
	"os"
	"strconv"
)

type Node struct {
	dist, index int
}

func (n Node) unpack() (int, int) {
	return n.dist, n.index
}

type HeapQ []Node

func (h HeapQ) Len() int {
	return len(h)
}

func (h HeapQ) Less(i, j int) bool {
	return h[i].dist < h[j].dist
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
	*h = old[:n-1]
	return x
}

func mst(N int, hq *HeapQ, graph [][]int) int {
	ans := 0
	visit := make([]bool, N)
	for hq.Len() > 0 {
		dist, now := heap.Pop(hq).(Node).unpack()

		if visit[now] {
			continue
		}
		visit[now] = true
		ans += dist
		for nxt := 0; nxt < N; nxt++ {
			if now == nxt {
				continue
			}
			heap.Push(hq, Node{graph[now][nxt], nxt})
		}
	}
	return ans
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	hq := &HeapQ{}
	heap.Init(hq)
	for i := 0; i < N; i++ {
		heap.Push(hq, Node{input(), i})
	}

	graph := make([][]int, N)
	for i := 0; i < N; i++ {
		graph[i] = make([]int, N)
		for j := 0; j < N; j++ {
			graph[i][j] = input()
		}
	}
	bw.WriteString(strconv.Itoa(mst(N, hq, graph)))
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
