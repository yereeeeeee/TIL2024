import sys; input = sys.stdin.readline
from collections import deque


'''
# 모듈러 연산

A mod B = C 이면, 임의의 수 D에 대하여
(A*D) mod B = (C*D) mod B
(A+D) mod B = (C+D) mod B
'''
def bfs(num):
    q = deque([('1')])
    visit = [False] * num
    while q:
        now = q.popleft()

        if int(now) % num == 0: return now
        if len(now) > 100: break
        
        for i in "01":
            nxt = now+i
            if visit[int(nxt) % num]: continue

            visit[int(nxt) % num] = True
            q.append(nxt)
    return "BRAK"

for _ in range(int(input())):
    print(bfs(int(input())))
