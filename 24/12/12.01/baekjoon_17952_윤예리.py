import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
time = n

curr = deque([])
answer = 0
for _ in range(n):
    tmp = list(map(int, input().split()))

    if tmp[0] == 0:
        if curr:
            a, t = curr.popleft()
            if t > 1:
                curr.appendleft([a, t-1])
            else:
                answer += a

    else:
        a, t = tmp[1], tmp[2]
        # 시간 안 남으면
        if t == 1:
            answer += a

        else:
            curr.appendleft([a, t-1])
print(answer)