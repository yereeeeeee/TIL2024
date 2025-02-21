'''
돌연변이

아호-코라식 / 해싱, 문자열

아호-코라식 연습 문제로 있길래 한 번 더 했다가, 온몸 비틀기로 해도 파이썬 아호-코라식으로 안풀리길래
일단 자바로 번역해서 품.

그리고 혹시나 해서 제일 원초적인 풀이로 풀었는데 됨.
왜됨? 이거 플2 문젠데
'''

# import sys; input = lambda: sys.stdin.readline().strip()
# from collections import deque


# def make_markers(pattern):
#     res = set()
#     for i in range(M):
#         for j in range(i+1,M+1):
#             res.add(pattern[:i] + pattern[i:j][::-1] + pattern[j:])
#     return res

# def insert(markers):
#     for marker in markers:
#         now = trie
#         for char in marker:
#             now = now.setdefault(char, dict())
#         now[0] = True
#     connect()

# def connect():
#     q = deque([trie])

#     while q:
#         now = q.popleft()

#         for char in now:
#             if char == 0 or char == 1: continue

#             nxt = now[char]

#             if now is trie:
#                 nxt[1] = trie
            
#             else:
#                 dst = now[1]
#                 while dst is not trie and char not in dst:
#                     dst = dst[1]
                
#                 if char in dst:
#                     dst = dst[char]
                
#                 nxt[1] = dst

#             if 0 in nxt[1]:
#                 nxt[0] = True
            
#             q.append(nxt)

# def search(word):
#     ans = 0

#     now = trie
#     for char in word:
#         while now is not trie and char not in now:
#             now = now[1]
        
#         if char in now:
#             now = now[char]
        
#         if 0 in now:
#             ans += 1
    
#     return ans


# for _ in range(int(input())):
#     N,M = map(int,input().split())
    
#     word = input()
#     pattern = input()

#     markers = make_markers(pattern)

#     trie = dict()
#     insert(markers)

#     print(search(word))

## 설마
import sys; input = lambda: sys.stdin.readline().strip()

def create_patterns(pattern):
    res = set()
    for i in range(M):
        for j in range(i+1, M+1):
            res.add(pattern[:i] + pattern[i:j][::-1] + pattern[j:])
    return res

for _ in range(int(input())):
    N,M = map(int,input().split())
    word = input()
    pattern = input()
    patterns = create_patterns(pattern)
    cnt = 0
    for i in range(N-M+1):
        p = word[i:i+M]
        if p in patterns:
            cnt += 1
    print(cnt)