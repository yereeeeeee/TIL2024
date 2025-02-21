'''
집 가고 싶다

다익스트라, 해시

해싱을 통해 장소에 대한 인덱스를 부여하고, 다익스트라를 통해 최단거리를 계산
'''


import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def djikstra(start, end):
    distance = [float('inf')] * (len(data)+1)
    hq = [(0,start)]
    distance[start] = 0
    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue

        for nxt,cost in graph[now]:
            dist_next = dist_now + cost
            if distance[nxt] > dist_next:
                distance[nxt] = dist_next
                heappush(hq, (dist_next, nxt))
    return distance[end]

data = dict()
data["sasa"] = 1
data["home"] = 2
graph = [[] for _ in range(3)]
for _ in range(int(input())):
    a,b,c = input().split()
    for i in a,b:
        if not data.get(i):
            data[i] = len(data)+1
            graph.append([])
    graph[data[a]].append((data[b],int(c)))

ans = djikstra(1,2) + djikstra(2,1)
print(ans if ans != float('inf') else -1)