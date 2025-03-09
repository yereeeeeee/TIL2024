'''
탈출

다익스트라
'''
import sys; input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush


dr = (1,0),(0,1),(-1,0),(0,-1)

def find(arr, char):
    N,M = len(arr), len(arr[0])
    res = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                res.append((i,j))
    return res

def merge(arr, brr):
    N,M = len(arr), len(arr[0])
    for i in range(N):
        for j in range(M):
            arr[i][j] += brr[i][j]
    return arr

def dijkstra(arr, start):
    sx,sy = start
    N,M = len(arr), len(arr[0])
    distance = [[float('inf')]*M for _ in range(N)]
    distance[sx][sy] = 0
    hq = [(0, sx,sy)]
    while hq:
        dist_now, x,y = heappop(hq)

        if dist_now > distance[x][y]: continue

        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == "*": continue
                dist_nxt = dist_now + (arr[nx][ny] == "#")
                
                if distance[nx][ny] > dist_nxt:
                    distance[nx][ny] = dist_nxt
                    heappush(hq, (dist_nxt, nx,ny))
    return distance

def solve():
    N,M = map(int,input().split())
    
    arr = [["."] * (M+2) for _ in range(N+2)]
    for i in range(1,N+1):
        tmp = input()
        for j in range(1,M+1):
            arr[i][j] = tmp[j-1]
    N += 2
    M += 2

    starts = find(arr, "$")
    starts.append((0,0))

    res = [[0] * M for _ in range(N)]
    for start in starts:
        res = merge(res, dijkstra(arr, start))
    
    ans = float('inf')
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "#":
                res[i][j] -= 2
            ans = min(ans, res[i][j])
    print(ans)

for _ in range(int(input())):
    solve()