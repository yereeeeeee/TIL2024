'''
그래프를 3차원으로 두고, 그래프 내부에 환승역만 배치해 다익스트라 탐색
역 노션의 앞, 뒤로 움직이는 것 또한 다익스트라 로직 내부에서 구현
'''
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(w, s1,s2, e1,e2):
    '''
    w: 가중치
    s1,s2: 시작 노선, 역
    e1,e2: 도착 노선, 역
    '''
    hq = [(0,s1,s2)]
    distance = [[float('inf') for _ in range(len(graph[i]))] for i in range(N+1)]
    distance[s1][s2] = 0
    while hq:
        dist_now,x,y = heappop(hq)
        if dist_now > distance[x][y]: continue
        # 환승
        for nx,ny in graph[x][y]:
            if distance[nx][ny] > dist_now + w:
                distance[nx][ny] = dist_now + w
                heappush(hq, (distance[nx][ny], nx, ny))
        # 노선 내부
        for i in -1, 1:
            if 1 <= (ny:=y+i) < len(graph[x]):
                if distance[x][ny] > dist_now + 1:
                    distance[x][ny] = dist_now + 1
                    heappush(hq, (distance[x][ny], x, ny))

    return distance[e1][e2]

N = int(input())

graph = [[], ]
for size in map(int,input().split()):
    graph.append([[] for _ in range(size+1)])

for _ in range(int(input())):
    p1,p2, q1,q2 = map(int,input().split())

    graph[p1][p2].append((q1,q2))
    graph[q1][q2].append((p1,p2))

for _ in range(int(input())):
    print(dijkstra(*map(int,input().split())))