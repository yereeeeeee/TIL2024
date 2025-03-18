package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	bs.Split(bufio.ScanWords)
	bs.Buffer(buf, 1024*1024)
	defer bw.Flush()

	group := input()
	password := input()
	length := len(group)

	data := make(map[string]int)
	for i := 0; i < length; i++ {
		data[string(group[i])] = i + 1
	}
	ans := 0
	for i := 0; i < len(password); i++ {
		ans *= length
		ans += data[string(password[i])]
		ans %= 900528
	}
	bw.WriteString(fmt.Sprintln(ans))
}

var (
	bs  = bufio.NewScanner(os.Stdin)
	bw  = bufio.NewWriter(os.Stdout)
	buf = make([]byte, 0, 1024*1024)
)

func input() string {
	bs.Scan()
	return bs.Text()
}
