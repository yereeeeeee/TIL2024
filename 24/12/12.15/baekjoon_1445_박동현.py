'''
일요일 아침의 데이트

다익스트라

쓰레기를 10000 으로, 쓰레기 옆길을 1로 두어 cost를 계산하고
이외에는 0으로 다익스트라를 돌려서 값을 나누어 계산한다.
'''

import sys; input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())

tmp = [list(input()) for _ in range(N)]
arr = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if tmp[i][j] == "S":
            si,sj = i,j
            continue
        if tmp[i][j] == "F":
            ei,ej = i,j
            continue
        if tmp[i][j] == "g":
            arr[i][j] += 10000
            for dx,dy in dr:
                di,dj = i+dx, j+dy
                if 0<=di<N and 0<=dj<M:
                    arr[di][dj] += 1
arr[si][sj] = 0
arr[ei][ej] = 0
hq = [(0,si,sj)]
distance = [[float('inf')]*M for _ in range(N)]
distance[si][sj] = 0

while hq:
    dist_now, x, y = heappop(hq)

    if dist_now > distance[x][y]: continue

    for dx,dy in dr:
        di,dj = x+dx, y+dy
        if 0<=di<N and 0<=dj<M:
            cost = 0 
            if arr[di][dj] >= 10000:
                cost = 10000
            elif arr[di][dj] > 0:
                cost = 1
            dist_nxt = dist_now + cost
            if distance[di][dj] > dist_nxt:
                distance[di][dj] = dist_nxt
                heappush(hq, (dist_nxt, di, dj))

print(distance[ei][ej]// 10000, distance[ei][ej] % 10000)