import sys; input = sys.stdin.readline


def floyd_warshall():
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i==j: continue
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


N = int(input())
graph = [[float('inf')]*(N+1) for _ in range(N+1)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a][b] = 1

floyd_warshall()
ans = [sum(0 if graph[i][j] != float('inf') or graph[j][i] != float('inf') else 1 for j in range(1,N+1))-1 for i in range(1,N+1)]
print(*ans, sep ="\n")