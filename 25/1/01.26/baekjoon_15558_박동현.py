'''
점프 게임

bfs

추가조건 달린 bfs
'''
from collections import deque


def cal(a,b):
    if b == K:
        return 1-a
    return a

def dfs():
    visit = [[0]*N for _ in range(2)]
    q = deque([(0,0)])
    while q:
        x, y = q.popleft()
        
        for dy in K,1,-1:
            ny = y+dy
            if ny >= N: return 1

            if ny <= visit[x][y]: continue
            nx = cal(x,dy)

            if arr[nx][ny] == "0": continue
            if visit[nx][ny]: continue
            visit[nx][ny] = visit[x][y] + 1
            q.append((nx,ny))
    return 0

N,K = map(int,input().split())
arr = [input() for _ in range(2)]
print(dfs())