import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


class Node:
    def __init__(self, idx):
        self.children = dict()
        self.fail = None
        self.end = 0
        self.idx = idx
    
class AhoCorasick:
    idx = 0

    def __init__(self, patterns):
        self.root = Node(self.idx)
        self.nodes = [self.root]
        
        for pattern in patterns:
            self.insert(pattern)
        self.connect()
    
    def insert(self, pattern):
        now = self.root
        for char in pattern:
            if char not in now.children:
                self.idx += 1
                new_node = Node(self.idx)
                now.children[char] = new_node
                self.nodes.append(new_node)
            now = now.children[char]
        now.end += 1

    def connect(self):
        q = deque([self.root])
        self.root.fail = self.root

        while q:
            now = q.popleft()
            for char, nxt in now.children.items():
                if now == self.root:
                    nxt.fail = self.root
                else:
                    dst = now.fail
                    while dst != self.root and char not in dst.children:
                        dst = dst.fail
                    if char in dst.children:
                        dst = dst.children[char]
                    nxt.fail = dst
                    nxt.end += nxt.fail.end
                q.append(nxt)

    def find(self, node, char):
        while node != self.root and char not in node.children:
            node = node.fail
        if char in node.children:
            node = node.children[char]
        else:
            node = self.root
        return node


N,M = map(int,input().split())
ac = AhoCorasick([input() for _ in range(N)])

node_count = len(ac.nodes)
DP = [[-1] * node_count for _ in range(M + 1)]
DP[0][0] = 0

for i in range(M):
    for now_index in range(node_count):
        if DP[i][now_index] == -1: continue

        now_node = ac.nodes[now_index]
        for char in "ABC":
            next_node = ac.find(now_node, char)
            next_value = DP[i][now_index]+next_node.end

            DP[i+1][next_node.idx] = max(DP[i+1][next_node.idx], next_value)

print(max(DP[M]))
