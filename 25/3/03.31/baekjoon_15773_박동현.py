import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N = int(input())
arr = sorted([[*map(int,input().split())] for _ in range(N)], key=lambda x: x[0]+x[1])

hq = []
now = 0

for L,D in arr:
    now += D
    heappush(hq, -D)
    
    if now > L + D:
        now += heappop(hq)

print(len(hq))