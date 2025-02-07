'''
배달

BFS, 비트마스킹 

해당 좌표에 들어온 방향으로 다시 들어오는 것은 의미 없는 행동이니 비트마스킹을 통해 컷한다.
'''
import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def multi_bfs(i,j):
    visit = [[-1]*M for _ in range(N)]
    dr = [[0]*M for _ in range(N)]
    visit[i][j] = 0
    
    q = deque([(i,j,-1)])
    answer = []
    while q:
        x,y,d = q.popleft()

        if arr[x][y] == "C":
            dist_nxt = bfs(x,y,d)
            if dist_nxt:
                answer.append(visit[x][y] + dist_nxt)

        for i in range(4):
            if i==d: continue
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if dr[nx][ny] & 1<<i: continue
                if arr[nx][ny] == "#": continue
                dr[nx][ny] |= 1<<i
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny,i))
    return answer

def bfs(ci, cj, d):
    visit = [[-1]*M for _ in range(N)]
    dr = [[0]*M for _ in range(N)]
    visit[ci][cj] = 0
    
    q = deque([(ci,cj,d)])
    while q:
        x,y,d = q.popleft()
        if not(x == ci and y == cj) and arr[x][y] == "C":
            return visit[x][y]

        for i in range(4):
            if d == i: continue
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if dr[nx][ny] & 1<<i: continue
                if arr[nx][ny] == "#": continue
                dr[nx][ny] |= 1<<i
                visit[nx][ny] = visit[x][y]+1
                q.append((nx,ny,i))
    return 0

def find(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                arr[i][j] = "."
                return i,j

dx = 1, 0, -1, 0
dy = 0, 1, 0, -1

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

answer = multi_bfs(*find("S"))
print(-1 if not answer else min(answer))
