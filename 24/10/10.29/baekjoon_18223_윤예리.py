import sys
input = sys.stdin.readline
from heapq import *

V, E, P = map(int, input().split())
graph = [[] for _ in range(V+1)]
distance = [10e9] * (V+1)

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for next_node, next_dist in graph[now]:
            if dist + next_dist < distance[next_node]:
                distance[next_node] = dist + next_dist
                heappush(q, (dist + next_dist, next_node))

    return distance

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 민준이가 마산까지 가는 거리가 민준이가 건우까지 가는 거리 + 건우가 마산까지 가는 거리라면
if dijkstra(1)[V] == dijkstra(1)[P] + dijkstra(P)[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")

