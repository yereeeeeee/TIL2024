package main

import (
	"bufio"
	"container/heap"
	"os"
	"strconv"
)

// Heap
type Node struct {
	value, idx int
}
type HeapQ []Node

func (h HeapQ) Len() int {
	return len(h)
}
func (h HeapQ) Less(i, j int) bool {
	if h[i].value < h[j].value {
		return true
	} else if h[i].value == h[j].value {
		return h[i].idx < h[j].idx
	} else {
		return false
	}
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

func makeEnumeratedHeap(idx int, lst []int, hq *HeapQ) {
	for i, v := range lst {
		heap.Push(hq, Node{v, i + idx})
	}
}

var (
	N     int
	arr   []int
	brr   []int
	arrHq = &HeapQ{}
	brrHq = &HeapQ{}
)

// Query
func U(x, y int) {
	if x <= N {
		heap.Push(arrHq, Node{y, x})
		arr[x-1] = y
	} else {
		heap.Push(brrHq, Node{y, x})
		brr[x-N-1] = y
	}
}

func L() {
	for (*arrHq)[0].value != arr[(*arrHq)[0].idx-1] {
		heap.Pop(arrHq)
	}
	for (*brrHq)[0].value != brr[(*brrHq)[0].idx-N-1] {
		heap.Pop(brrHq)
	}
	bw.WriteString(strconv.Itoa((*arrHq)[0].idx) + " " + strconv.Itoa((*brrHq)[0].idx) + "\n")
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()
	N = inputInt()
	M := inputInt()
	// arr
	arr = make([]int, N)
	for i := range arr {
		arr[i] = inputInt()
	}
	heap.Init(arrHq)
	makeEnumeratedHeap(1, arr, arrHq)
	// brr
	brr = make([]int, M)
	for i := range brr {
		brr[i] = inputInt()
	}
	heap.Init(brrHq)
	makeEnumeratedHeap(N+1, brr, brrHq)

	// Query
	Q := inputInt()
	for i := 0; i < Q; i++ {
		cmd := input()
		if cmd == "U" {
			x, y := inputInt(), inputInt()
			U(x, y)
		} else {
			L()
		}
	}
}

// fastIO
var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() string {
	bs.Scan()
	return bs.Text()
}

func inputInt() int {
	num, _ := strconv.Atoi(input())
	return num
}
