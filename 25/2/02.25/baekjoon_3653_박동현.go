package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

type SegTree []int

func (st SegTree) Init(node, start, end int, arr []int) {
	if start == end {
		st[node] = arr[start]
		return
	}
	mid := (start + end) / 2

	st.Init(node*2, start, mid, arr)
	st.Init(node*2+1, mid+1, end, arr)

	st[node] = st[node*2] + st[node*2+1]
}

func (st SegTree) Update(node, start, end, idx, diff int) {
	if !(start <= idx && idx <= end) {
		return
	}
	st[node] += diff
	if start == end {
		return
	}

	mid := (start + end) / 2
	st.Update(node*2, start, mid, idx, diff)
	st.Update(node*2+1, mid+1, end, idx, diff)
}

func (st SegTree) Query(node, start, end, left, right int) int {
	if end < left || right < start {
		return 0
	}
	if left <= start && end <= right {
		return st[node]
	}

	mid := (start + end) / 2
	leftSum := st.Query(node*2, start, mid, left, right)
	rightSum := st.Query(node*2+1, mid+1, end, left, right)
	return leftSum + rightSum
}

func solve() {

	N, M := input(), input()
	arr := make([]int, N+M)
	for i := M; i < M+N; i++ {
		arr[i] = 1
	}

	position := make([]int, N+1)
	for i := 1; i < N+1; i++ {
		position[i] = i + M - 1
	}
	size := 1 << (int(math.Ceil(math.Log2(float64(N+M)))) + 1)
	segTree := make(SegTree, size)
	segTree.Init(1, 0, N+M-1, arr)

	movies := make([]int, M)
	for i := 0; i < M; i++ {
		movies[i] = input()
	}
	top := M - 1
	for _, movie := range movies {

		segTree.Update(1, 0, N+M-1, position[movie], -1)

		bw.WriteString(strconv.Itoa(segTree.Query(1, 0, M+N-1, 0, position[movie]-1)) + " ")
		position[movie] = top
		top--

		segTree.Update(1, 0, N+M-1, position[movie], +1)
	}
	bw.WriteString("\n")
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	tc := input()
	for i := 0; i < tc; i++ {
		solve()
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
