# 그리디 어려워서 적응하고자 실버 한 문제 풀어봄

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in  range(n)]

answer = 0

for coin in reverse(arr):
    if k >= coin:
        answer += k // coin
        k %= coin

print(answer)