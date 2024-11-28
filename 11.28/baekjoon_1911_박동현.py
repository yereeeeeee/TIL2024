'''
흙길 보수하기

스위핑

M길이의 판자를 사용하기 위해 개수를 계산하고, 이어붙이기
'''


import sys; input = sys.stdin.readline
from math import ceil


N,M = map(int,input().split())
arr = sorted([[*map(int,input().split())] for _ in range(N)])

now,cnt = 0,0
for s,e in arr:
    # 시작점이 이미 멀리 있는 경우 
    if s > now:
        tmp = ceil((e-s) / M)
        cnt += tmp
        now = s + tmp * M
        continue

    # 시작점은 now보다 크거나 같은데, 끝점은 더 멀리 있는 경우
    # now가 s를 일부분 덮고 있으니 now부터 e 까지 보수하면 됨
    if e > now:
        tmp = ceil((e-now) / M)
        cnt += tmp
        now = now + tmp*M
print(cnt)