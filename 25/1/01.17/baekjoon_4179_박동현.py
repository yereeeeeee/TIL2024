'''
불!

BFS

불 한 칸, 사람 한 칸 번갈아가며 움직이기
'''
import sys; input = lambda: sys.stdin.readline().strip()


def find(char):
    res = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                visit[i][j] = 1
                res.append((i,j))
    return res

def bfs_fire():
    next_fires = []
    while fires:
        x,y = fires.pop()

        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == "#": continue
                if arr[nx][ny] == "F": continue
                if visit[nx][ny]: continue
                arr[nx][ny] = "F"
                next_fires.append((nx,ny))
    return next_fires

def bfs_man():
    global ans

    next_mans = []
    while mans:
        x,y = mans.pop()
        if x == 0 or x == N-1 or y == 0 or y == M-1:
            ans = visit[x][y]
            return
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] != ".": continue
                if visit[nx][ny]: continue
                visit[nx][ny] = visit[x][y] + 1
                next_mans.append((nx,ny))
    return next_mans


dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

visit = [[0]*M for _ in range(N+1)]
mans = find("J")
fires = find("F")

ans = 0
while not ans and mans:
    fires = bfs_fire()
    mans = bfs_man()

print(ans if ans else "IMPOSSIBLE")