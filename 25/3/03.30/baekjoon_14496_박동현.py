import sys; input = sys.stdin.readline
from collections import deque


def bfs(start, end):
    visit = [-1] * (N+1)
    visit[start] = 0
    q = deque([start])
    while q:
        now = q.popleft()

        if now == end: break

        for nxt in graph[now]:
            if visit[nxt] != -1: continue
            visit[nxt] = visit[now] + 1
            q.append(nxt)

    return visit[end]


s,e = map(int,input().split())
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(s,e))