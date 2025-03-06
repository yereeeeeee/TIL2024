package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

type Heapq []Node

func (h Heapq) Len() int {
	return len(h)
}

func (h Heapq) Less(i, j int) bool {
	return h[i].x < h[j].x
}

func (h Heapq) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *Heapq) Push(x interface{}) {
	*h = append(*h, x.(Node))
}

func (h *Heapq) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type Node struct {
	x, y int
}

func (n Node) unpack() (int, int) {
	return n.x, n.y
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()
	N, M := input(), input()

	costs := make([]int, N+1)
	for i := 1; i < N+1; i++ {
		costs[i] = input()
	}

	graph := make([][]Node, N+1)
	for i := 0; i < N+1; i++ {
		graph[i] = make([]Node, 0)
	}

	for i := 0; i < M; i++ {
		a, b, c := input(), input(), input()
		graph[b] = append(graph[b], Node{a, c})
		graph[c] = append(graph[c], Node{a, b})
	}

	hq := &Heapq{}
	heap.Init(hq)
	for i := 1; i < N+1; i++ {
		hq.Push(Node{costs[i], i})
	}

	for hq.Len() > 0 {
		cost_now, now := hq.Pop().(Node).unpack()

		if cost_now > costs[now] {
			continue
		}

		for _, node := range graph[now] {
			prod, comp := node.unpack()
			if costs[prod] > cost_now+costs[comp] {
				costs[prod] = cost_now + costs[comp]
				hq.Push(Node{costs[prod], prod})
			}
		}
	}
	bw.WriteString(fmt.Sprintln(costs[1]))
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
