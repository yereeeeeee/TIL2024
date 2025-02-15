'''
로봇 청소기

외판원 순회, BFS

지독하게도 섞어놨다.
'''
import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


dr = (1,0),(0,1),(-1,0),(0,-1)

def bfs(x,y,i):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()



        for dx,dy in dr:
            nx,ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny] != -1: continue
                if arr[nx][ny] == "x": continue

                if arr[nx][ny] == "*":
                    j = position[(nx,ny)]

                    if not dist[i][j]:
                        dist[i][j] = dist[j][i] = visit[x][y] + 1
                        left[i] -= 1
                        if i: left[j] -= 1
                        if not left[i]: return 0
                
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))
    return True

def check(now=0, bit=1):
    if bit == max_v-1: return 0
    if DP[now][bit] > 0: return DP[now][bit]

    tmp = float('inf')
    for idx, w in enumerate(dist[now]):
        if bit & 1<<idx: continue
        tmp = min(tmp, check(idx, bit|1<<idx)+w)
    DP[now][bit] = tmp
    return tmp

while True:
    M,N = map(int,input().split())
    if N==M==0: break

    arr = [input() for _ in range(N)]
    position = dict()
    cnt = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "*":
                position[(i,j)] = cnt
                cnt += 1
            elif arr[i][j] == "o":
                position[(i,j)] = 0

    dist = [[0]*cnt for _ in range(cnt)]
    left = [cnt-2] * cnt
    left[0] += 1

    for (x,y), idx in position.items():
        if not left[idx]: continue
        visit = [[-1]*M for _ in range(N)]
        visit[x][y] = 0
        if bfs(x,y, idx):
            print(-1)
            break
    else:
        max_v = 1<<cnt
        DP = [[0]*max_v for _ in range(cnt)]
        print(check())