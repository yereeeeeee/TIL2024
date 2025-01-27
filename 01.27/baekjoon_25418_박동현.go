/*
* 정수 a를 k로 만들기
*
* DP, bfs
*
* go 연습
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	br = bufio.NewReader(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func main() {
	defer bw.Flush()

	var A, K int
	fmt.Fscanln(br, &A, &K)

	DP := make([]int, K+1)

	for i := A + 1; i <= K; i++ {
		if i/2 >= A && i%2 == 0 && DP[i/2] < DP[i-1] {
			DP[i] = DP[i/2] + 1
		} else {
			DP[i] = DP[i-1] + 1
		}
	}
	bw.WriteString(strconv.Itoa(DP[K]))
}
