import sys; input = sys.stdin.readline
from heapq import heappop, heappush

def mst(graph):
    visit = [False]*(N+1)
    hq = [(0,0)]
    res = 0
    while hq:
        dist, now = heappop(hq)
        if visit[now]: continue

        visit[now] = True
        res += dist
        for nxt in graph[now]:
            heappush(hq, nxt)
    return res

N,M = map(int,input().split())
max_graph = [[] for _ in range(N+1)]
min_graph = [[] for _ in range(N+1)]
for i in range(M+1):
    a,b,c = map(int,input().split())
    max_graph[a].append((c,b))
    max_graph[b].append((c,a))
    min_graph[a].append((1-c,b))
    min_graph[b].append((1-c,a))

max_v = (N-mst(max_graph))**2
min_v = mst(min_graph)**2
print(max_v-min_v)