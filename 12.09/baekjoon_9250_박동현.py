'''
문자열 집합 판별

아호 코라식

딕셔너리로 만든 트라이 구조로 아호 코라식도 날먹할 수 있지 않을까? 하는 생각에 온몸 비틀기를 해봤지만 안된다.
단순히 0을 문자열 마지막으로 두는 정도는 괜찮은데, 실패 링크를 같이 넣어서 판별하는건 쉽지 않다.

일단 간단한 방법이 있나 더 찾아보고, 할 수 있으면 간단한 방법으로 풀고 싶음
클래스로 구현하는게 썩 마음에 들지는 않음

* 아호 코라식? KMP + 트라이다.
'''
import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


class Node:
    def __init__(self,key=""):
        self.key = key
        self.children = dict()
        self.fail = None
        self.is_end = False


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

                if now == self.root:
                    nxt.fail = self.root
                
                else:
                    dst = now.fail
                    while dst != self.root and char not in dst.children:
                        dst = dst.fail
                    
                    if char in dst.children:
                        dst = dst.children[char]
                    nxt.fail = dst
                
                if nxt.fail.is_end:
                    nxt.is_end = True
                q.append(nxt)
    
    def search(self, word):
        now = self.root

        for char in word:
            while now != self.root and char not in now.children:
                now = now.fail
            if char in now.children:
                now = now.children[char]
            if now.is_end:
                return True
        return False

ac = AhoCorasick([input() for _ in range(int(input()))])

words = [input() for _ in range(int(input()))]
for word in words:
    print("YES" if ac.search(word) else "NO")