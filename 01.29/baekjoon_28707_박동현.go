package main

import (
	"bufio"
	"container/heap"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

// MAX_VALUE 상수 정의
const (
	MAX_VALUE = math.MaxInt32
)

// fastIO
var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func input() int {
	bs.Scan()
	res, _ := strconv.Atoi(bs.Text())
	return res
}

// 쿼리 구조체, 메서드
type Query struct {
	a, b, cost int
}

func (q Query) unpack() (int, int, int) {
	return q.a, q.b, q.cost
}

// 노드 구조체, 메서드
type Node struct {
	key  string
	cost int
}

func (n Node) unpack() (string, int) {
	return n.key, n.cost
}

// Heap 관련 정의
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

// 메인 로직 함수
func arrToStr(arr []int) string {
	strArr := make([]string, len(arr))
	for i, v := range arr {
		strArr[i] = strconv.Itoa(v)
	}
	return strings.Join(strArr, ",")
}

func swap(a, b int, str string) string {
	strArr := strings.Split(str, ",")
	strArr[a], strArr[b] = strArr[b], strArr[a]
	return strings.Join(strArr, ",")
}

// main 함수
func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	arr := make([]int, N+1)
	for i := 1; i <= N; i++ {
		arr[i] = input()
	}
	M := input()
	query := make([]Query, M)
	for i := 0; i < M; i++ {
		query[i] = Query{input(), input(), input()}
	}
	start := arrToStr(arr)
	sort.Ints(arr)
	end := arrToStr(arr)
	distance := make(map[string]int)
	distance[start] = 0
	hq := &HeapQ{}
	heap.Init(hq)

	heap.Push(hq, Node{start, 0})

	for hq.Len() > 0 {
		now, distNow := heap.Pop(hq).(Node).unpack()

		for _, q := range query {
			a, b, cost := q.unpack()
			next := swap(a, b, now)
			distNext := distNow + cost
			if _, exists := distance[next]; !exists {
				distance[next] = MAX_VALUE
			}
			if distance[next] > distNext {
				distance[next] = distNext
				heap.Push(hq, Node{next, distNext})
			}
		}
	}

	if value, exists := distance[end]; exists {
		bw.WriteString(strconv.Itoa(value))
	} else {
		bw.WriteString("-1")
	}
}
