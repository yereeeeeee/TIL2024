import sys; input=sys.stdin.readline; sys.setrecursionlimit(50001)
from math import ceil, log2


def dfs(now=1, d=0, dist=0):    
    visit[now] = True
    depth[now] = d

    for nxt, cost in graph[now]:
        if visit[nxt]: continue
        parent[nxt][0] = now
        distance[nxt] = dist+cost
        dfs(nxt, d+1, dist+cost)

def build_sparse_table():
    for j in range(1,LOG):
        for i in range(1, N+1):
            if parent[i][j-1]:
                parent[i][j] = parent[parent[i][j-1]][j-1]

def lca(a,b):
    if depth[a] < depth[b]:
        a,b = b,a
    
    diff = depth[a] - depth[b]
    for i in range(LOG):
        if diff & (1<<i):
            a = parent[a][i]
    
    if a == b:
        return a

    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

### INPUT ###
N = int(input())
LOG = ceil(log2(N))

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

visit = [False] * (N+1)
depth = [0] * (N+1)
parent = [[0] * LOG for _ in range(N+1)]
distance = [0] * (N+1)

dfs()
build_sparse_table()

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(distance[a] + distance[b] - distance[lca(a,b)]*2)