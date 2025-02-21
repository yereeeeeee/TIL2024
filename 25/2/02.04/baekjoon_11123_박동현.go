package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"strconv"
)

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)

	dx = [4]int{1, 0, -1, 0}
	dy = [4]int{0, 1, 0, -1}
)

type Node struct {
	x, y int
}

func (n Node) unpack() (int, int) {
	return n.x, n.y
}

func solve() {
	N, M := inputInt(), inputInt()

	arr := make([]string, N)
	for i := 0; i < N; i++ {
		arr[i] = input()
	}

	visit := make([][]bool, N)
	for i := 0; i < N; i++ {
		visit[i] = make([]bool, M)
	}

	ans := 0
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			if arr[i][j] == '#' && !visit[i][j] {
				visit[i][j] = true
				bfs(N, M, i, j, &visit, arr)
				ans++
			}
		}
	}
	bw.WriteString(fmt.Sprintln(ans))
}

func bfs(N, M, i, j int, visit *[][]bool, arr []string) {
	q := list.New()

	q.PushBack(Node{i, j})
	for q.Len() > 0 {
		x, y := q.Remove(q.Front()).(Node).unpack()
		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]
			if 0 <= nx && nx < N && 0 <= ny && ny < M && !(*visit)[nx][ny] && arr[nx][ny] == '#' {
				(*visit)[nx][ny] = true
				q.PushBack(Node{nx, ny})
			}
		}
	}
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()
	tc := inputInt()
	for i := 0; i < tc; i++ {
		solve()
	}
}

func inputInt() int {
	num, _ := strconv.Atoi(input())
	return num
}

func input() string {
	bs.Scan()
	return bs.Text()
}
