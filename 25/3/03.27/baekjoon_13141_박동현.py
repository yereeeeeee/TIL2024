import sys; input = sys.stdin.readline


def floyd_warshall():
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1, N+1):
                if i==j: continue
                min_graph[i][j] = min_graph[j][i] = min(min_graph[i][j], min_graph[i][k] + min_graph[k][j])

def ignite(s):
    res = 0
    for i in range(1,N+1):
        for j in range(i,N+1):
            if not max_graph[i][j]: continue
            a,b = min_graph[s][i], min_graph[s][j]
            remain = max_graph[i][j] - abs(b-a)
            res = max(res, max(a,b) + remain/2)
    return res

N,M = map(int,input().split())
min_graph = [[float('inf')] * (N+1) for _ in range(N+1)]
max_graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    min_graph[a][b] = min_graph[b][a] = min(min_graph[a][b], c)
    max_graph[a][b] = max_graph[b][a] = max(max_graph[a][b], c)

floyd_warshall()
ans = float('inf')
for i in range(1,N+1):
    min_graph[i][i] = 0
    ans = min(ans, ignite(i))
print(f"{ans:.01f}")
