'''
Emoticons :-)

아호-코라식

아호-코라식을 통해 문자열에 있는 패턴을 찾아내고,
중복을 제외하기 위해 추가적인 예외처리를 한다.
'''

import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


class Node:
    def __init__(self,key=""):
        self.key = key
        self.children = dict()
        self.is_end = False
        self.fail = None


class AhoCorasick:
    def __init__(self, patterns):
        self.root = Node()
        for pattern in patterns:
            self.insert(pattern)
        self.connect()
    
    def insert(self, pattern):
        now = self.root

        for char in pattern:
            now = now.children.setdefault(char, Node(char))
        now.is_end = True
    
    def connect(self):
        q = deque([self.root])
        while q:
            now = q.popleft()
            for char in now.children:
                nxt = now.children[char]
                if now is self.root:
                    nxt.fail = self.root
                
                else:
                    dst = now.fail
                    while dst is not self.root and char not in dst.children:
                        dst = dst.fail
                    
                    if char in dst.children:
                        dst = dst.children[char]
                    
                    nxt.fail = dst

                if nxt.fail.is_end: nxt.is_end = True

                q.append(nxt)
    
    def search(self, word):
        now = self.root
        ans = 0
        for char in word:
            while now is not self.root and char not in now.children:
                now = now.fail
            
            if char in now.children:
                now = now.children[char]
            
            if now.is_end:
                ans += 1
                now = self.root
        return ans
                



while True:
    N,M = map(int,input().split())
    if N == M == 0 : break

    ac = AhoCorasick([input() for _ in range(N)])
    ans = 0
    for _ in range(M):
        ans += ac.search(input())
    print(ans)