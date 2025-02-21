'''
수열과 쿼리 20

트라이

트라이를 기반으로 쿼리를 해결하는 문제
XOR문제의 확장판
'''

import sys; input = sys.stdin.readline


class Node:
    def __init__(self, key=""):
        self.key = key
        self.children = dict()
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, binary):
        now = self.root

        for char in binary:
            now = now.children.setdefault(int(char), Node(char))
            now.cnt += 1
    
    def delete(self, binary):
        now = self.root

        for char in binary:
            now = now.children[int(char)]
            now.cnt -= 1

    def search(self, binary):
        now = self.root
        ans = ""
        for char in binary:
            check = 1-int(char)

            if check in now.children and now.children[check].cnt:
                now = now.children[check]
                ans += "1"
                
            elif 1-check in now.children and now.children[1-check].cnt:
                now = now.children[1-check]
                ans += "0"
                
        return print(int(ans,2))


# 2**30 > 10**9
def create_binary(num):
    return bin(num)[2:].zfill(30)

query = {
    1: lambda x: trie.insert(x),
    2: lambda x: trie.delete(x),
    3: lambda x: trie.search(x)
}

trie = Trie()
trie.insert(create_binary(0))
for _ in range(int(input())):
    a, x = map(int,input().split())
    query[a](create_binary(x))