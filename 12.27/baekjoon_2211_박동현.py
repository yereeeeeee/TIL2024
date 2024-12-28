'''
네트워크 복구

다익스트라

사용한 간선을 찾아달라는 문제
visit 배열에 사용한 간선을 담아 계산
'''
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [float('inf')] * (N+1)
distance[1] = 0
hq = [(0,1)]

visit = [[] for _ in range(N+1)]
while hq:
    dist_now, now = heappop(hq)
    if dist_now > distance[now]: continue

    for nxt, cost in graph[now]:
        dist_nxt = dist_now + cost
        if distance[nxt] > dist_nxt:
            distance[nxt] = dist_nxt
            visit[nxt] = visit[now][:] + [(now,nxt) if now < nxt else (nxt,now)]
            heappush(hq, (dist_nxt, nxt))

answer = {item for v in visit for item in v}

print(len(answer))
for ans in answer:
    print(*ans)