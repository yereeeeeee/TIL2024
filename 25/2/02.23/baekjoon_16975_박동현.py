import sys; input = sys.stdin.readline
from math import ceil, log2


class SegTree:
    def __init__(self, N, arr):
        size = 1 << (ceil(log2(N)) + 1)
        self.arr = arr
        self.tree = [0] * size
        self.lazy = [0] * size

        self.init_seg_tree(1,0,N-1)
    
    def init_seg_tree(self, node, start, end):
        if start == end: 
            self.tree[node] = self.arr[start]
            return
        mid = (start+end) // 2
        self.init_seg_tree(node*2, start, mid)
        self.init_seg_tree(node*2+1, mid+1, end)
    
    def update_lazy(self, node, start, end):
        if self.lazy[node]:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[node*2] += self.lazy[node]
                self.lazy[node*2+1] += self.lazy[node]
            self.lazy[node] = 0
    
    def update_range(self, node, start, end, left, right, diff):
        self.update_lazy(node, start, end)

        if left > end or right < start: return

        if left <= start and end <= right:
            self.tree[node] += diff

            if start != end:
                self.lazy[node*2] += diff
                self.lazy[node*2+1] += diff
            return
        
        mid = (start+end) // 2

        self.update_range(node*2, start, mid, left, right, diff)
        self.update_range(node*2+1, mid+1, end, left, right, diff)

    def query(self, node, start, end, target):

        self.update_lazy(node, start, end)
        if target == start == end: return self.tree[node]
        
        mid = (start+end) // 2
        if target <= mid:
            return self.query(node*2, start, mid, target)
        else:
            return self.query(node*2+1, mid+1, end, target)


N = int(input())
arr = [*map(int,input().split())]

seg_tree = SegTree(N, arr)

cmd = {
    1: lambda left,right,diff: seg_tree.update_range(1, 0, N-1, left-1, right-1, diff),
    2: lambda x: print(seg_tree.query(1, 0, N-1, x-1))
}
for _ in range(int(input())):
    a, *q = map(int,input().split())
    cmd[a](*q)