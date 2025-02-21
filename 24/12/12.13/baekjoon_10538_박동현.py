'''
빅 픽쳐

kmp 해싱 아호-코라식

그냥 문자열로 할 수 있는 모든 것
이거 안보고 제대로 구현할 수 있으면 더 이상 문자열 알고리즘 빡세게 안해도 될 것 같음

패턴을 트라이에 담고, 실패 노드 연결
이를 기반으로 2차원 배열을 순회하면서 visit배열 생성

외부에서는 kmp 배열을 만들고, 생성해둔 visit 배열과 함께 순회하며 탐색
'''
import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


class Node:
    def __init__(self, key=""):
        self.key = key
        self.fail = None
        self.children = dict()
        self.is_end = -1


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word, idx):
        now = self.root

        for char in word:
            now = now.children.setdefault(char, Node(char))
        now.is_end = idx

    def connect(self):
        q = deque([self.root])
        while q:
            now = q.popleft()

            for char in now.children:
                nxt = now.children[char]

                if now is self.root:
                    nxt.fail = now
                
                else:
                    dst = now.fail

                    while dst is not self.root and char not in dst.children:
                        dst = dst.fail
                    
                    if char in dst.children:
                        dst = dst.children[char]
                    
                    nxt.fail = dst
                
                if nxt.fail.is_end != -1:
                    nxt.is_end = nxt.fail.is_end

                q.append(nxt)
    
    def match(self, N, M, arr):
        visit = [[-1] * M for _ in range(N)]

        for i in range(N):
            now = self.root
            for j in range(M):
                char = arr[i][j]
                while now is not self.root and char not in now.children:
                    now = now.fail
                if char in now.children:
                    now = now.children[char]
                
                if now.is_end != -1:
                    visit[i][j] = now.is_end
        return visit


X,Y, N,M = map(int,input().split())

patterns = [tuple([1 if x =="o" else 0 for x in input()]) for _ in range(X)]
arr = [tuple([1 if x =="o" else 0 for x in input()]) for _ in range(N)]

keys = dict()
knum = list()

ac = AhoCorasick()
# 해싱하여 리스트에 저장하고, 트라이에 입력
for i in range(X):
    pattern = patterns[i]
    if pattern not in keys:
        keys[pattern] = i
        ac.insert(pattern, i)
    knum.append(keys[pattern])
# 실패 노드 생성
ac.connect()


# KMP 배열 생성
kmp = [0]*X
k = 0
for i in range(1, X):
    while k > 0 and knum[i] != knum[k]:
        k = kmp[k-1]
    if knum[i] == knum[k]:
        k += 1
    kmp[i] = k

# 아호 코라식 전처리
visit = ac.match(N,M,arr)

# 결과 계산
ans = 0
for j in range(M):
    k = 0
    for i in range(N):
        while k > 0 and visit[i][j] != knum[k]:
            k = kmp[k-1]
        
        if visit[i][j] == knum[k]:
            if k == X-1:
                ans += 1
                k = kmp[k]
            else:
                k += 1
print(ans)