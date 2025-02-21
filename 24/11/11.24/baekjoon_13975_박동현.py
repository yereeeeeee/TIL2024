'''
파일 합치기 3

우선순위 큐
'''


import sys; input=sys.stdin.readline
from heapq import heappop, heappush, heapify


def merge_file():
    return heappop(hq) + heappop(hq)


for _ in range(int(input())):
    N = int(input())
    hq = [*map(int,input().split())]
    heapify(hq)
    ans = 0
    for _ in range(N-1):
        file = merge_file()
        ans += file
        heappush(hq, file)
    print(ans)