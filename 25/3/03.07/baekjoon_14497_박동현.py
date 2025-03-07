import sys; input = sys.stdin.readline
from heapq import heappop, heappush


dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
sx,sy, ex,ey = map(lambda x: int(x)-1, input().split())
arr = [input() for _ in range(N)]


hq = [(0, sx,sy)]
distance = [[float('inf')] * M for _ in range(N)]
distance[sx][sy] = 0

while hq:
    dist_now, x,y = heappop(hq)
    if dist_now > distance[x][y]: continue

    for dx, dy in dr:
        nx,ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            dist_nxt = dist_now + (arr[nx][ny] != "0")
            if distance[nx][ny] > dist_nxt:
                distance[nx][ny] = dist_nxt
                heappush(hq, (dist_nxt, nx, ny))
print(distance[ex][ey])
