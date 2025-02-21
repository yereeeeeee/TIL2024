import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = [[-1] * n for _ in range(n)]

def dfs(x, y):
    if cnt[x][y] != -1:
        return cnt[x][y]
    cnt[x][y] = 1
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:
            cnt[x][y] = max(cnt[x][y], dfs(nx, ny) + 1)
    return cnt[x][y]

for i in range(n):
    for j in range(n):
        if cnt[i][j] == -1:
            dfs(i, j)

answer = max(max(row) for row in cnt)
print(answer)
