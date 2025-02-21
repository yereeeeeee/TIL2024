'''
할로윈의 양아치

유니온 파인드, 배낭 문제

파이썬 시간초과를 해결할 수가 없어요
pypy: 113680kb, 492ms
go: 1548kb, 100ms
'''
import sys; input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y: return

    if root_x > root_y: root_x, root_y = root_y, root_x

    parent[root_y] = root_x
    arr[root_x] += arr[root_y]
    cnt[root_x] += cnt[root_y]

N,M,K = map(int,input().split())
arr = [0] + [*map(int,input().split())]

parent = [*range(N+1)]
cnt = [1] * (N+1)
for _ in range(M):
    union(*map(int,input().split()))

DP = [0] * K
for ch, cd in sorted([(cnt[i], arr[i]) for i in range(1,N+1) if i == parent[i] and cnt[i] <= K]):
    for i in range(K-1, ch-1, -1):
        DP[i] = max(DP[i], DP[i-ch] + cd)

print(DP[-1])