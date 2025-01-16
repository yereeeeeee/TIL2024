'''
인터넷 설치

다익스트라, 이분 탐색

이분 탐색의 매개 변수를 다익스트라로 구현
'''
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(num):
    
    cnt = [float('inf')] * (N+1)
    cnt[1] = 0
    hq = [(0,1)]
    while hq:
        cnt_now, now = heappop(hq)

        if cnt_now > cnt[now]: continue

        for nxt,cost in graph[now]:
            cnt_next = cnt_now + int(cost > num)
            if cnt[nxt] > cnt_next:
                cnt[nxt] = cnt_next
                heappush(hq, (cnt_next, nxt))
    return cnt[N] <= K


N,P,K = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(P):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

left, right = 0, 1000000
ans = -1
while left <= right:
    mid = (left+right) // 2

    if dijkstra(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)