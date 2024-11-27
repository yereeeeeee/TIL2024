'''
연료 채우기

그리디

주유소의 위치와 연료량을 정렬하고, 
갈 수 있는 곳들을 하나씩 우선순위 큐에 담아서 하나씩 넣어서 
최소 cnt로 마을에 도착할 수 있도록 계산함

유사한 방식의 문제가 있었는데,
입력 자체를 힙으로 만들지 말고, 가능한 부분만 힙으로 구현해야 하는 듯
'''

import sys; input = sys.stdin.readline
from heapq import heappop, heappush


arr = sorted([[*map(int,input().split())] for _ in range(int(input()))], reverse=True)
goal, now = map(int,input().split())

cnt = 0
hq = []
while goal > now:
    while arr and arr[-1][0] <= now:
        dist, fuel = arr.pop()
        heappush(hq, -fuel)

    if not hq: exit(print(-1))

    now -= heappop(hq)
    cnt += 1
print(cnt)
