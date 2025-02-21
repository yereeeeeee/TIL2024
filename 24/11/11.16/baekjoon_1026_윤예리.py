import sys
input = sys.stdin.readline
from heapq import *

n = int(input())
arr = list(map(int, input().split()))
tmp_b = list(map(int, input().split()))
brr = []

answer = 0
heapify(arr)
for i in range(n):
    heappush(brr, -tmp_b[i])

for _ in range(n):
    answer += heappop(arr) * heappop(brr) * -1

print(answer)