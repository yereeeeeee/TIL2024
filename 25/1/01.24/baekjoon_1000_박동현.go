/*
* A + B
*
* go 해보려고. 엘라스틱 서치랑 이것저것 써봐야함
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var input = bufio.NewScanner(os.Stdin)

func main() {
	input.Scan()
	nums := strings.Split(input.Text(), " ")
	a, _ := strconv.Atoi(nums[0])
	b, _ := strconv.Atoi(nums[1])

	fmt.Println(a + b)
}
