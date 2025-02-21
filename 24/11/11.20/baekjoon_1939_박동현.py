'''
중량제한

N개의 섬, M개의 다리
A,B,C는 A번 섬과 B번 섬 사이에 중량 제한이 C 인 다리가 존재 (양방향)
1<= C <= 1,000,000,000

이분 탐색, BFS
'''

import sys; input = sys.stdin.readline
from collections import deque


def bfs(limit):
    visit = [False]*(N+1)
    visit[start] = True
    q = deque([start])

    while q:
        now = q.popleft()

        if now == end:
            return True

        for nxt, cost in graph[now]:
            if cost >= limit and not visit[nxt]:
                q.append(nxt)
                visit[nxt] = True
    return False

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for i in range(N+1):
    graph[i].sort(reverse=True)

start,end = map(int,input().split())
left,right = 1,1000000000
while left<=right:
    mid = (left+right) // 2

    if bfs(mid):
        left = mid+1
    else:
        right = mid-1

print(right)