package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
)

var (
	br = bufio.NewReader(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
	dr = [2]int{-1, 1}
)

type Node struct {
	x, y int
}

func (n Node) unpack() (int, int) {
	return n.x, n.y
}

func bfs(arr []string, N, K int) string {
	visit := make([][]int, 2)
	for i := range visit {
		visit[i] = make([]int, N)
	}
	q := list.New()
	q.PushBack(Node{0, 0})
	for q.Len() > 0 {
		x, y := q.Remove(q.Front()).(Node).unpack()

		for i := 0; i < 2; i++ {
			ny := y + dr[i]

			if ny >= N {
				return "1"
			}

			if ny >= 0 && ny > visit[x][y] {
				if arr[x][ny] == '1' && visit[x][ny] == 0 {
					visit[x][ny] = visit[x][y] + 1
					q.PushBack(Node{x, ny})
				}
			}
		}

		ny := y + K
		if ny >= N {
			return "1"
		}
		if ny <= visit[x][y] {
			continue
		}
		if arr[1-x][ny] == '0' {
			continue
		}
		if visit[1-x][ny] != 0 {
			continue
		}
		visit[1-x][ny] = visit[x][y] + 1
		q.PushBack(Node{1 - x, ny})
	}
	return "0"
}

func main() {
	defer bw.Flush()

	var N, K int
	fmt.Fscanln(br, &N, &K)

	arr := make([]string, 2)
	for i := range arr {
		var tmp string
		fmt.Fscanln(br, &tmp)
		arr[i] = tmp
	}

	bw.WriteString(bfs(arr, N, K))
}
