package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func find(arr []int, idx int) int {
	target := arr[idx]
	res := 0
	for i := idx; i < len(arr); i++ {
		if target == arr[i] {
			res++
		} else {
			break
		}
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N := input()
	A, B, C, D := make([]int, N), make([]int, N), make([]int, N), make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = input()
		B[i] = input()
		C[i] = input()
		D[i] = input()
	}
	AB := make([]int, N*N)
	CD := make([]int, N*N)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			AB[i*N+j] = A[i] + B[j]
			CD[i*N+j] = C[i] + D[j]
		}
	}
	sort.Ints(AB)
	sort.Sort(sort.Reverse(sort.IntSlice(CD)))

	ab, cd := 0, 0
	ans := 0
	for ab < N*N && cd < N*N {
		total := AB[ab] + CD[cd]
		if total == 0 {
			abCnt := find(AB, ab)
			cdCnt := find(CD, cd)
			ans += abCnt * cdCnt
			ab += abCnt
			cd += cdCnt
		} else if total > 0 {
			cd += find(CD, cd)
		} else {
			ab += find(AB, ab)
		}
	}
	bw.WriteString(strconv.Itoa(ans))
}

func input() int {
	bs.Scan()
	num, _ := strconv.Atoi(bs.Text())
	return num
}
