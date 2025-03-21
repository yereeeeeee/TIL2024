package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	arr []string
)

func check(arr []string) bool {
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr[0]); j++ {
			if arr[i][j] != arr[j][i] {
				return false
			}
		}
	}
	return true
}

func backtrack(idx, bit int, res []int) {
	if idx == len(res) {
		result := make([]string, len(res))
		for i := 0; i < len(res); i++ {
			result[i] = arr[res[i]]
		}
		if check(result) {
			for _, v := range result {
				bw.WriteString(v + "\n")
			}
			panic("a")
		}
		return
	}

	for i := 0; i < len(arr); i++ {
		if bit&(1<<i) > 0 {
			continue
		}
		if idx > 0 && arr[res[0]][idx] != arr[i][0] {
			continue
		}

		res[idx] = i
		backtrack(idx+1, bit|1<<i, res)
		res[idx] = -1

	}
}

func main() {
	bs.Split(bufio.ScanWords)
	defer func() {
		bw.Flush()
		if r := recover(); r == "a" {
			return
		}
	}()

	L, N := inputInt(), inputInt()
	arr = make([]string, N)

	for i := 0; i < N; i++ {
		arr[i] = input()
	}
	sort.Strings(arr)

	backtrack(0, 0, make([]int, L))
	bw.WriteString("NONE")
}

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
