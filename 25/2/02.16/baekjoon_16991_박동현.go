package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

const MAX_VALUE = 1e5

var (
	N   int
	DP  [][]float64
	arr [][]float64
)

type Node struct {
	x, y int
}

func square(num int) int {
	return num * num
}

func calcDistance(a, b Node) float64 {
	return math.Sqrt(float64(square(a.x-b.x) + square(a.y-b.y)))
}

func tsp(now, bit int) float64 {
	if bit == (1<<N)-1 {
		return arr[now][0]
	}
	if DP[now][bit] != 0 {
		return DP[now][bit]
	}

	minValue := MAX_VALUE
	for next := 1; next < N; next++ {
		if bit&(1<<next) > 0 {
			continue
		}
		cost := tsp(next, bit|(1<<next)) + arr[now][next]
		minValue = min(minValue, cost)
	}
	DP[now][bit] = minValue
	return minValue
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N = input()
	pos := make([]Node, N)
	for i := 0; i < N; i++ {
		x, y := input(), input()
		pos[i] = Node{x, y}
	}
	arr = make([][]float64, N)
	for i := 0; i < N; i++ {
		arr[i] = make([]float64, N)
	}
	for i := 0; i < N-1; i++ {
		for j := i + 1; j < N; j++ {
			distance := calcDistance(pos[i], pos[j])
			arr[i][j] = distance
			arr[j][i] = distance
		}
	}
	DP = make([][]float64, N)
	for i := 0; i < N; i++ {
		DP[i] = make([]float64, 1<<N)
	}

	ans := tsp(0, 1)
	bw.WriteString(fmt.Sprintln(ans))
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
