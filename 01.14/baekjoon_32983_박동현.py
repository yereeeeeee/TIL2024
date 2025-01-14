import sys; input = sys.stdin.readline
from collections import deque


def bfs():
    res = 0
    new_q = deque()
    while q:
        x,y = q.popleft()
        
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == -1: continue
                if visit[nx][ny]: continue

                visit[nx][ny] = True
                res += arr[nx][ny]
                new_q.append((nx,ny))
    return new_q, res


dr = (1,0),(0,1),(-1,0),(0,-1)

N,M,C = map(int,input().split())
sx,sy = map(lambda x: int(x)-1,input().split())

arr = [[*map(int,input().split())] for _ in range(N)]

visit = [[False]*M for _ in range(N)]
visit[sx][sy] = True
q = deque([(sx,sy)])
answer = [arr[sx][sy]]
while q:
    q,ans = bfs()
    answer.append(ans-C+answer[-1])

print(max(answer))