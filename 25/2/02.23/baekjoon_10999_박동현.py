import sys; input = sys.stdin.readline
from math import ceil,log2


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    
    else:
        mid = (start+end) // 2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2 + 1]

def update_lazy(node, start, end):
    if lazy[node]:
        tree[node] += (end-start+1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update_range(node, start, end, left, right, diff):
    update_lazy(node, start, end)
    if left > end or right < start: return
    
    if left <= start and end <= right:
        tree[node] += (end-start+1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    mid = (start+end) // 2
    update_range(node*2, start, mid, left, right, diff)
    update_range(node*2+1, mid+1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(node, start, end, left, right):
    update_lazy(node, start, end)
    
    if left > end or right < start: return 0
    
    if left <= start and end <= right: return tree[node]

    mid = (start+end) // 2
    left_sum = query(node*2, start, mid, left, right)
    right_sum = query(node*2+1, mid+1, end, left, right)
    return left_sum + right_sum

N,M,K = map(int,input().split())
arr = [int(input()) for _ in range(N)]
h = ceil(log2(N)) + 1
size = 1<<h

tree = [0] * size
lazy = [0] * size


init(1,0,N-1)

cmd = {
    1: lambda left, right, diff: update_range(1, 0, N-1, left-1, right-1, diff),
    2: lambda left, right: print(query(1, 0, N-1, left-1, right-1))
}

for _ in range(M+K):
    a, *q = map(int,input().split())
    cmd[a](*q)
