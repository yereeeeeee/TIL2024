package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
	"strconv"
)

const (
	MAX_VALUE = math.MaxInt32
)

var (
	br = bufio.NewReader(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

type Node struct {
	idx, value int
}

func (n Node) unpack() (int, int) {
	return n.idx, n.value
}

type HeapQ []Node

func (h HeapQ) Len() int {
	return len(h)
}

func (h HeapQ) Less(i, j int) bool {
	return h[i].value < h[j].value
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

func dijkstra(graph [][]Node, start int) []int {
	hq := &HeapQ{}
	heap.Init(hq)

	heap.Push(hq, Node{start, 0})
	distance := make([]int, len(graph))
	for i := range distance {
		distance[i] = MAX_VALUE
	}
	distance[start] = 0

	for hq.Len() > 0 {
		now, distNow := heap.Pop(hq).(Node).unpack()

		if distNow > distance[now] {
			continue
		}

		for _, nextNode := range graph[now] {
			next, cost := nextNode.unpack()
			distNext := distance[now] + cost
			if distance[next] > distNext {
				distance[next] = distNext
				heap.Push(hq, Node{next, distNext})
			}
		}
	}
	return distance
}

func main() {
	defer bw.Flush()

	var N, M, start int
	fmt.Fscanln(br, &N, &M)
	fmt.Fscanln(br, &start)

	graph := make([][]Node, N+1)
	for i := 0; i < M; i++ {
		var a, b, c int
		fmt.Fscanln(br, &a, &b, &c)
		graph[a] = append(graph[a], Node{b, c})
	}

	distance := dijkstra(graph, start)

	for _, d := range distance[1:] {
		if d == MAX_VALUE {
			bw.WriteString("INF" + "\n")
		} else {
			bw.WriteString(strconv.Itoa(d) + "\n")
		}
	}
}
