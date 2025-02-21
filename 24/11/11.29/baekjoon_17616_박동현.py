'''
등수 찾기

그래프, BFS, DFS

관계가 주어졌을 때, 탐색을 이용해 가능한 등수를 계산한다.
근데 굳이 dfs bfs 하나씩 쓸 이유는 없는 것 같음
'''

import sys; input = sys.stdin.readline
from collections import deque


def dfs(graph):
    cnt = 0
    visit = [False]*(N+1)
    stack = [X]
    while stack:
        now = stack.pop()

        if visit[now]: continue
        visit[now] = True
        cnt += 1
        for nxt in graph[now]:
            stack.append(nxt)
    return cnt
 
def bfs(graph):

    visit = [False]*(N+1)
    visit[X] = True
    q = deque([X])
    cnt = 0
    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if not visit[nxt]:
                q.append(nxt)
                visit[nxt] = True
                cnt += 1
    return cnt

N,M,X = map(int,input().split())

graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    rev_graph[b].append(a)


print(dfs(rev_graph))
print(N-bfs(graph))