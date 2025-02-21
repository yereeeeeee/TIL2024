'''
상범 빌딩

BFS

토마토 빌딩
'''
import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


def find(word):
    for i in range(N):
        for j in range(M):
            for k in range(K):
                if arr[i][j][k] == word:
                    return i,j,k

def bfs():
    si,sj,sk = find("S")
    q = deque([(si,sj,sk)])
    visit = [[[0]*K for _ in range(M)] for _ in range(N)]
    visit[si][sj][sk] = 1
    while q:
        x,y,z = q.popleft()
        if arr[x][y][z] == "E":
            return f"Escaped in {visit[x][y][z]-1} minute(s)."
        for dx,dy,dz in dr:
            nx,ny,nz = x+dx, y+dy, z+dz
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < K:
                if visit[nx][ny][nz]: continue
                if arr[nx][ny][nz] == "#": continue
                visit[nx][ny][nz] = visit[x][y][z] + 1
                q.append((nx,ny,nz))
    return "Trapped!"

dr = (0,1,0),(0,0,1),(0,-1,0),(0,0,-1),(1,0,0),(-1,0,0)
while True:
    N,M,K = map(int,input().split())
    if N == M == K == 0: break

    arr = []
    for i in range(N):
        arr.append([list(input()) for _ in range(M)])
        input()
    
    print(bfs())