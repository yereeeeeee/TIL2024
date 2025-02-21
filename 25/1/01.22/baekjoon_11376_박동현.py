'''
열혈강호 2

이분 매칭

한 사람이 최대 2개의 일을 할 수 있다.
그렇다면, pair_a 배열의 길이를 두 배로 늘리면 되지 않을까?
'''
import sys; input = sys.stdin.readline
from collections import deque

def cal(num):
    return num%N if num%N else N

def bfs():
    q = deque()
    for i in range(1,2*N+1):
        if pair_a[i]:
            distance[i] = float('inf')
        else:
            distance[i] = 0
            q.append(i)
    distance[0] = float('inf')

    while q:
        now = q.popleft()

        if distance[now] < distance[0]:
            for nxt in graph[cal(now)]:
                if distance[pair_b[nxt]] == float('inf'):
                    distance[pair_b[nxt]] = distance[now] + 1
                    q.append(pair_b[nxt])
    return distance[0] != float('inf')

def dfs(now):
    if now:
        for nxt in graph[cal(now)]:
            if distance[pair_b[nxt]] == distance[now] + 1 and dfs(pair_b[nxt]):
                pair_a[now] = nxt
                pair_b[nxt] = now
                return True
        distance[now] = float('inf')
        return False
    return True

N,M = map(int,input().split())
graph = [[]]
for _ in range(N):
    num, *jobs = map(int,input().split())
    graph.append(jobs)

pair_a = [0]*(2*N+1)
pair_b = [0]*(M+1)
distance = [0]*(2*N+1)
ans = 0
while bfs():
    for i in range(1,2*N+1):
        if not pair_a[i] and dfs(i):
            ans += 1
print(ans)