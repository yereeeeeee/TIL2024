package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	br = bufio.NewReader(os.Stdin)
	bw = bufio.NewWriter(os.Stdout)
)

func reverse(s string) string {
	runes := []rune(s)

	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	defer bw.Flush()

	var str string
	fmt.Fscanln(br, &str)

	for i := 0; i < len(str); i++ {
		if str[i:] == reverse(str[i:]) {
			fmt.Fprintln(bw, len(str)+i)
			return
		}
	}
}
