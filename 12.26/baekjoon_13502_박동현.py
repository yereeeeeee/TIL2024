patterns = '''
문제 참조. 생략
'''

class Node:
    def __init__(self):
        self.children = dict()
        self.is_end = None


class Trie:
    def __init__(self, patterns):
        self.root = Node()
        self.ans = set()
        
        for pattern in patterns:
            self.insert(pattern)
    
    def insert(self, pattern):
        now = self.root
        for char in pattern:
            now = now.children.setdefault(char, Node())
        now.is_end = pattern
    
    def dfs(self, x, y, visit, now):
        
        for dx,dy in dr:
            di,dj = x+dx, y+dy

            if 0 <= di < 5 and 0 <= dj < 5:
                if visit[di][dj]: continue
                if arr[di][dj] not in now.children: continue
                nxt = now.children[arr[di][dj]]
                if nxt.is_end: self.ans.add(nxt.is_end)
                visit[di][dj] = True
                self.dfs(di, dj, visit, nxt)
                visit[di][dj] = False


dr = (1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)

trie = Trie(patterns.split("\n"))

arr = [input().split() for _ in range(5)]
for i in range(5):
    for j in range(5):
        if arr[i][j] not in trie.root.children: continue
        visit = [[False]*5 for _ in range(5)]
        visit[i][j] = True
        trie.dfs(i, j, visit, trie.root.children[arr[i][j]])
print(len(trie.ans))