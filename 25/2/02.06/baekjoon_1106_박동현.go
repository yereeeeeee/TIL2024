package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const MAX_VALUE = math.MaxInt32

var (
	bs = bufio.NewScanner(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

type Advertise struct {
	cost, value int
}

func (a Advertise) unpack() (int, int) {
	return a.cost, a.value
}

func arrMinInt(arr []int) int {
	res := MAX_VALUE
	for _, n := range arr {
		res = min(res, n)
	}
	return res
}

func main() {
	bs.Split(bufio.ScanWords)
	defer bw.Flush()

	N, M := input(), input()
	arr := make([]Advertise, M)
	for i := 0; i < M; i++ {
		arr[i] = Advertise{cost: input(), value: input()}
	}

	DP := make([]int, N+101)
	for i := 1; i < len(DP); i++ {
		DP[i] = MAX_VALUE
	}

	for _, a := range arr {
		c, v := a.unpack()
		for i := v; i < len(DP); i++ {
			DP[i] = min(DP[i], DP[i-v]+c)
		}
	}
	bw.WriteString(strconv.Itoa(arrMinInt(DP[N:])))
}

func input() int {
	bs.Scan()
	num, _ := strconv.Atoi(bs.Text())
	return num
}
