# 최소 스패닝 트리 1197

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# cost 기준으로 작은 것 부터 정렬
edges.sort(key=lambda x:x[2])

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    parent[y] = x

def isSame(x, y):
    return find(x) == find(y)

answer = 0
for a, b, cost in edges:
    # 사이클 없을 때 최소 스패닝 트리
    if not isSame(a, b):
        union(a, b)
        answer += cost

print(answer)