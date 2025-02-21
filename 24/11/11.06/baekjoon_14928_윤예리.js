const fs = require("fs");
// let input = fs.readFileSync("input.txt").toString().trim(); // window에서 input 넣어서 확인하려면 txt 파일 받아야함
let input = fs.readFileSync("/dev/stdin").toString().trim(); // 백준 제출용
let n = BigInt(input); // 숫자가 커서 Bigint로 변경
console.log((n % 20000303n).toString()); // Bigint 뒤에 n이 붙어서 string으로 변경해서 print
