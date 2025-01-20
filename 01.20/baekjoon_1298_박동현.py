'''
노트북의 주인을 찾아서

이분 매칭

이분 매칭이란?

이분 그래프에서 가능한 최대 매칭을 찾는 문제
'''
'''
1번 풀이.
DFS 기반으로 문제를 해석하고, 각 노드에서 DFS를 반복 수행해 매칭을 시도한다.
이 경우, 큰 그래프에서는 반복 호출이 발생할 수 있고, 이로 인해 성능 저하가 발생할 수 있다.
메모리 사용량 자체는 상대적으로 적어, 단순한 이분 매칭 문제의 경우 사용할 수 있다.

시간 복잡도: O(E V)

import sys; input = sys.stdin.readline


def bi_match(now):

    if visit[now]: return False

    visit[now] = True

    for nxt in graph[now]:
        if not connection[nxt] or bi_match(connection[nxt]):
            connection[nxt] = now
            return True
    return False

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

connection = [0]*(N+1)
for i in range(N+1):
    visit = [False] * (N+1)
    bi_match(i)

print(sum(1 for x in connection if x))
'''

'''
2번 풀이.
Hopcraft-Karp 알고리즘을 사용한다.

BFS로 모든 경로를 찾고, 그 이후에 DFS로 병렬 처리를 수행한다.
가능한 여러 경로를 한 번에 갱신하기 때문에 1번 풀이에 비해 시간적인 이점이 발생한다.

시간 복잡도: O(E sqrt(V))
'''
import sys; input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque()
    for i in range(1,N+1):
        if pair_a[i]:
            distance[i] = float('inf')
        else:
            distance[i] = 0
            q.append(i)
    distance[0] = float('inf')

    while q:
        now = q.popleft()

        if distance[now] < distance[0]:
            for nxt in graph[now]:
                if distance[pair_b[nxt]] == float('inf'):
                    distance[pair_b[nxt]] = distance[now] + 1
                    q.append(pair_b[nxt])

    return distance[0] != float('inf')

def dfs(now):
    if now:
        for nxt in graph[now]:
            if distance[pair_b[nxt]] == distance[now] + 1 and dfs(pair_b[nxt]):
                pair_a[now] = nxt
                pair_b[nxt] = now
                return True
        distance[now] = float('inf')
        return False
    return True


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

pair_a = [0]*(N+1)
pair_b = [0]*(N+1)
distance = [0]*(N+1)

ans = 0
while bfs():
    for i in range(1, N+1):
        if not pair_a[i] and dfs(i):
            ans += 1
print(ans)