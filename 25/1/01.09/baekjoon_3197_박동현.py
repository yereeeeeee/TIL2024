'''
백조의 호수

BFS

중복 체크를 확실하게 해야 한다. visit를 두고도 중복이 발생할 수 있다.
'''
import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def find(x):
    res = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == x:
                res.append((i,j))
    return res

def change(x,y):
    arr[x][y] = "."

def bfs():
    res = []
    while swan:
        x,y = swan.popleft()
        
        if (x,y) == other_swan: return False
        
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if visit[nx][ny]: continue
                visit[nx][ny] = True
                if arr[nx][ny] == "X":
                    res.append((nx,ny))
                    continue
                swan.append((nx,ny))
    return deque(res)

def ice_brake():
    res = []
    while water: 
        x,y = water.pop()
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == "X":
                    res.append((nx,ny))
                    arr[nx][ny] = "."
    return res


dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

swan, other_swan = find("L")
for s in swan,other_swan: change(*s)
swan = deque([swan])

water = find(".")
cnt = 0
while swan:=bfs():
    water = ice_brake()
    cnt += 1
print(cnt)