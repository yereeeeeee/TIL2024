import sys; input = sys.stdin.readline
from collections import deque


class Edge:
    def __init__(self):
        self.capacity = 0
        self.flow = 0


def bfs(start, end):
    path = [0] * (N+1)
    q = deque([start])
    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if path[nxt]: continue

            if graph[now][nxt].capacity - graph[now][nxt].flow > 0:
                path[nxt] = now
                if nxt == end: return path
                q.append(nxt)
    return 0

def edmonds_karp(start, end):
    res = 0
    while (path:=bfs(start, end)):
        min_cap = float('inf')

        now = end
        while now != start:
            prev = path[now]
            min_cap = min(min_cap, graph[prev][now].capacity - graph[prev][now].flow)
            now = prev
        
        now = end
        while now != start:
            prev = path[now]
            graph[prev][now].flow += min_cap
            graph[now][prev].flow -= min_cap
            now = prev

        res += min_cap
    return res


N,M = map(int,input().split())
graph = [dict() for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].setdefault(b, Edge()).capacity += c
    graph[b].setdefault(a, Edge()).capacity += c

print(edmonds_karp(*map(int,input().split())))