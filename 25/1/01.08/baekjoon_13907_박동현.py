'''
세금

다익스트라

벽 뚫고 이동하기 2
딕셔너리로 distance를 만들어 실행한 경우 python 시간초과, pypy 4500ms가 나왔다.
'''
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra():

    def is_valid():
        for i in range(cnt+1):
            if distance[now][i] < dist_now:
                return False
        return True
    
    distance = [[float('inf')]*N for _ in range(N+1)]
    distance[S][0] = 0
    hq = [(0,0,S)]

    while hq:
        dist_now, cnt, now = heappop(hq)
        if cnt == N-1: continue
        if not is_valid(): continue

        for nxt, cost in graph[now]:
            dist_nxt = dist_now + cost
            if distance[nxt][cnt+1] > dist_nxt:
                distance[nxt][cnt+1] = dist_nxt
                heappush(hq, (dist_nxt, cnt+1, nxt))

    return distance[D]

N,M,K = map(int,input().split())
S,D = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = dijkstra()

taxes = [0]+[int(input()) for _ in range(K)]
pay = 0
last_idx = N-1
for tax in taxes:
    pay += tax 
    ans = float('inf')
    for idx in range(1, last_idx+1):
        cost = distance[idx] + idx*pay
        if ans > cost:
            ans = cost
            last_idx = idx
    print(ans)
