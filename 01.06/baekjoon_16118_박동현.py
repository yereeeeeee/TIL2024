'''
달빛 여우

다익스트라

distance를 2차원으로 나누어서 생각하기
'''
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra_for_fox():
    distance = [float('inf')]*(N+1)
    distance[1] = 0
    hq = [(0,1)]
    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue
        for nxt, cost in graph[now]:
            dist_nxt = dist_now + cost
            if distance[nxt] > dist_nxt:
                distance[nxt] = dist_nxt
                heappush(hq, (dist_nxt, nxt))

    return distance

def dijkstra_for_wolf():
    # 0: 걸어서 도착, 1: 뛰어서 도착
    distance = [[float('inf')]*2 for _ in range(N+1)]
    distance[1][0] = 0

    hq = [(0,1,True)]
    while hq:
        dist_now, now, is_runable = heappop(hq)

        if dist_now > distance[now][1-is_runable]: continue

        for nxt, cost in graph[now]:
            dist_nxt = dist_now + cost/2 if is_runable else dist_now + cost*2
            if distance[nxt][is_runable] > dist_nxt:
                distance[nxt][is_runable] = dist_nxt
                heappush(hq, (dist_nxt, nxt, not is_runable))

    return distance


N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

fox = dijkstra_for_fox()
wolf = dijkstra_for_wolf()

print(sum(f<min(w) for f,w in zip(fox,wolf)))