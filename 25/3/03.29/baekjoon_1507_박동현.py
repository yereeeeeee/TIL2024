import sys; input = sys.stdin.readline


def floyd_warshall():
    visit = [[True]*N for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j or i == k or k == j: continue
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    return -1
                if arr[i][j] == arr[i][k] + arr[k][j]:
                    visit[i][j] = visit[j][i] = False
    
    ans  = 0
    for i in range(N):
        for j in range(i, N):
            if visit[i][j]: ans += arr[i][j]
    return ans


N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]

print(floyd_warshall())