const fs = require("fs"); // 입력 받기
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n"); // 입력 받은 내용 줄 바꿈 처리
let [nums] = input; // 배열에 저장
let [n1, k1, n2, k2] = nums.split(" ").map((value) => +value); // split 처리
console.log(n1 * k1 + n2 * k2);
