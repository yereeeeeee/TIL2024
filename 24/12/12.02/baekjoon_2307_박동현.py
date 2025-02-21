'''
도로검문

다익스트라, 역추적

최단거리 - 한 도로를 제외한 최단 거리 를 찾는 문제
모든 다리를 막는 로직을 구성했을 때 시간 초과가 발생
모든 다리를 막아보는 게 아니라 최단거리를 지난 도로 중 하나만 막으면 되기 때문에
결국, 역추적을 통해 건너온 다리를 찾는 다익스트라 역추적 문제로 귀결된다. 
'''
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def trace_back(distance, route):
    now = route[-1]

    if now == 1:
        return route
    
    for prev,cost in graph[now]:
        if distance[prev] == distance[now] - cost:
            return trace_back(distance, route+[prev])

def dijkstra(ban=None):
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    hq = [(0,1)]

    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue
        for nxt, cost in graph[now]:
            if {now,nxt} == ban: continue
            dist_nxt = dist_now + cost
            if distance[nxt] > dist_nxt:
                distance[nxt] = dist_nxt
                heappush(hq,(dist_nxt, nxt))
    # 최단 거리를 찾는 경우 역추적을 위한 ban을 저장
    if not ban:
        banned.extend(trace_back(distance, [N]))
    return distance[-1]

# 용의자의 출발점은 1, 도착점은 N
N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
banned = []
for _ in range(M):
    a,b,cost = map(int,input().split())

    graph[a].append((b,cost))
    graph[b].append((a,cost))

ans = dijkstra()

time = 0
for i in range(len(banned)-1):
    ban = { banned[i], banned[i+1] }
    time = max(time, dijkstra(ban))

ans = time - ans
print(-1 if ans == float('inf') else ans)