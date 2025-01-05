'''
공주님을 구해라!

BFS

2에 도달한 순간 맨하튼 거리로 계산, 이외에는 일반 BFS
'''
import sys; input = sys.stdin.readline
from collections import deque


dr = (0,1),(1,0),(-1,0),(0,-1)

N,M,K = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

q = deque([(0,0)])
visit = [[0]*M for _ in range(N)]
visit[0][0] = 1

ans = float('inf')
while q:
    i,j = q.popleft()
    if (i,j) == (N-1,M-1):
        ans = min(ans, visit[i][j]-1)
        break

    for di,dj in dr:
        ni,nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<M:
            if visit[ni][nj]: continue
            if arr[ni][nj] == 1: continue

            visit[ni][nj] = visit[i][j] + 1

            if arr[ni][nj] == 2:
                ans = min(ans, visit[ni][nj] - 1 + (N-1 - ni) + (M-1 - nj))
            elif arr[ni][nj] == 0:
                q.append((ni,nj))

print(ans if ans <= K else "Fail")