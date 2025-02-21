'''
개코전쟁

다익스트라, 역추적

그냥 역추적 문제. 비슷한거 저번에 풀었었음
'''

import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(check = None):
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    hq = [(0,1)]
    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue
        
        for nxt, cost in graph[now]:
            if check == {nxt,now}: continue
            dist_nxt = dist_now + cost

            if distance[nxt] > dist_nxt:
                distance[nxt] = dist_nxt
                heappush(hq, (dist_nxt, nxt))
    if check is None:
        return distance
    else:
        return distance[-1]

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
distance = dijkstra()

# 역추적
tmp = [N]
while tmp[-1] != 1:
    for nxt,cost in graph[tmp[-1]]:
        if distance[tmp[-1]]-cost == distance[nxt]:
            tmp.append(nxt)

banned = []
for i in range(len(tmp)-1):
    banned.append({tmp[i],tmp[i+1]})


ans = 0
for ban in banned:
    ans = max(ans,dijkstra(ban))
print(ans)