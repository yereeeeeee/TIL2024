'''
대표 선수

우선순위 큐, 투 포인터

포인터를 기반으로 우선순위 큐를 구현.
'''
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N,M = map(int,input().split())
arr = [ ]
hq, max_v = [], 0
for i in range(N):
    tmp = sorted([*map(int,input().split())])

    arr.append(tmp)
    max_v = max(max_v, tmp[0])
    heappush(hq, (tmp[0], i))

ans = float('inf')

pointer = [0]*N
while True:
    value, idx = heappop(hq)
    ans = min(ans, max_v - value)

    if pointer[idx] == M-1: break

    pointer[idx] += 1
    heappush(hq, (arr[idx][pointer[idx]], idx))
    max_v = max(max_v, arr[idx][pointer[idx]])

print(ans)