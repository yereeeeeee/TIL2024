'''
접두사 찾기

트라이 복습
'''

import sys; input = sys.stdin.readline


def insert(string):
    now = Trie

    for char in string:
        now = now.setdefault(char, dict())


def check(string):
    now = Trie
    for char in string:
        if char in now:
            now = now[char]
        else:
            return False
    return True


N,M = map(int,input().split())

Trie = dict()
for _ in range(N):
    insert(input().strip())

ans = 0
for _ in range(M):
    ans += check(input().strip())

print(ans)