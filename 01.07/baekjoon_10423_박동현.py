'''
전기가 부족해

MST

시작점이 많은 그패프 탐색처럼, 시작점이 많은 MST로 취급
'''

import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N,M,K = map(int,input().split())
hq = [(0,x) for x in map(int, input().split())]

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

visit = [False] * (N+1)

ans = 0
while hq:
    cost, now = heappop(hq)

    if visit[now]: continue
    visit[now] = True
    ans += cost
    for nxt in graph[now]: heappush(hq, nxt)

print(ans)