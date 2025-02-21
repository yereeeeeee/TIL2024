package main

import (
	"bufio"
	"container/list"
	"os"
	"strconv"
	"strings"
)

var (
	br = bufio.NewReader(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

var (
	dx = []int{0, 1, 0, -1}
	dy = []int{1, 0, -1, 0}
)

func input() string {
	line, _, _ := br.ReadLine()
	return string(line)
}

type Node struct {
	x, y int
}

func main() {
	size := strings.Fields(input())
	N, _ := strconv.Atoi(size[0])
	M, _ := strconv.Atoi(size[1])

	var arr [][]bool
	var visit [][]int
	for i := 0; i < N; i++ {
		line := input()
		row := make([]bool, M)
		v := make([]int, M)
		for j, ch := range line {
			if ch == '1' {
				row[j] = true
			} else {
				row[j] = false
			}
		}
		arr = append(arr, row)
		visit = append(visit, v)
	}

	q := list.New()
	q.PushBack(Node{0, 0})
	visit[0][0] = 1

	defer bw.Flush()
	for q.Len() > 0 {
		now := q.Remove(q.Front()).(Node)
		x, y := now.x, now.y

		if x == N-1 && y == M-1 {
			bw.WriteString(strconv.Itoa(visit[x][y]))
			break
		}

		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]

			if 0 <= nx && nx < N && 0 <= ny && ny < M && arr[nx][ny] && visit[nx][ny] == 0 {
				q.PushBack(Node{nx, ny})
				visit[nx][ny] = visit[x][y] + 1
			}
		}
	}
}
