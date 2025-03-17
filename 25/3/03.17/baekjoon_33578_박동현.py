import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


dr = (1,0),(0,1),(-1,0),(0,-1)

def bfs(sx,sy, cost):
    visit = [[-1] * M for _ in range(N)]
    visit[sx][sy] = 0

    q = deque([(sx,sy)])
    while q:
        x, y = q.popleft()
        for dx, dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == "#": continue
                if visit[nx][ny] != -1: continue
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
    
    for i in range(N):
        for j in range(M):
            if visit[i][j] != -1:
                visit[i][j] *= cost
    return visit

def find(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                return i, j

N,M = map(int, input().split())
arr = [input() for _ in range(N)]
sx,sy = find("J")
ex,ey = find("S")

d0 = bfs(sx,sy, 2)
d1 = bfs(ex,ey, 1)

ans = float('inf')

if d0[ex][ey] != -1:
    ans = min(ans, d0[ex][ey])

for i in range(N):
    for j in range(M):
        if arr[i][j] == "T" and d0[i][j] != -1 and d1[i][j] != -1:
            ans = min(ans, d0[i][j] + d1[i][j])

print(-1 if ans == float('inf') else ans)
