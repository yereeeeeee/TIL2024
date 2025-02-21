'''
정복자

최소 스패닝 트리

최소 스패닝 트리 기본기.
추가적으로 정복할 때마다 늘어나는 비용을 cnt를 기반으로 계산
'''

import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N,M,K = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

visit = [False]*(N+1)
hq = [(0,1)]
ans,cnt = 0,0
while hq:
    dist_now, now = heappop(hq)

    if not visit[now]:
        visit[now] = True
        ans += dist_now
        cnt += 1
        if cnt > 2: ans += (cnt-2)*K

        for nxt, cost in graph[now]:
            heappush(hq, (cost, nxt))

print(ans)