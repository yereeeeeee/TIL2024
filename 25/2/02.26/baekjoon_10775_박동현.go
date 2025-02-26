package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type disjointSet []int

func (ds disjointSet) Find(x int) int {
	if ds[x] != x {
		ds[x] = ds.Find(ds[x])
	}
	return ds[x]
}

func (ds disjointSet) Union(x int, y int) {
	rootX := ds.Find(x)
	rootY := ds.Find(y)

	if rootX == rootY {
		return
	}

	if rootX < rootY {
		rootX, rootY = rootY, rootX
	}

	ds[rootX] = rootY
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	G := input()
	parent := make(disjointSet, G+1)
	for i := 0; i < G+1; i++ {
		parent[i] = i
	}

	P := input()
	planes := make([]int, P)
	for i := 0; i < P; i++ {
		planes[i] = input()
	}

	ans := 0
	for _, plane := range planes {
		x := parent.Find(plane)
		if x == 0 {
			break
		}
		parent.Union(x, x-1)
		ans++
	}
	fmt.Println(ans)
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
