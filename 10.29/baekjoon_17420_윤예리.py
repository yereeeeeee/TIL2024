import sys
input = sys.stdin.readline
import math

n = int(input())
left = list(map(int, input().split()))
use = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.append([left[i], use[i]])
# 빨리 써야 하는 것, 남은 기간이 얼마 없는 것
arr.sort(key=lambda x: (x[1], x[0]))

max_day = arr[0][0]
cur = arr[0][1]

cnt = 0
for i in range(n):
    # 연장
    if cur > arr[i][0]:
        tmp = math.ceil((cur - arr[i][0]) / 30)
        cnt += tmp
        arr[i][0] += tmp * 30

    max_day = max(max_day, arr[i][0])

    if i+1 < n and arr[i][1] != arr[i+1][1]:
        cur = max(max_day, arr[i+1][1])

print(cnt)