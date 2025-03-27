import sys; input = sys.stdin.readline


def floyd_warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i==j: continue
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

N,M = map(int,input().split())
distance = [[0 if i==j else float('inf') for i in range(N+1)] for j in range(N+1)] 
for _ in range(M):
    a,b = map(int,input().split())
    distance[a][b] = 1
floyd_warshall()

ans = 0
for i in range(1,N+1):
    if all(min(distance[i][j], distance[j][i]) != float('inf') for j in range(1,N+1)): ans += 1
print(ans)