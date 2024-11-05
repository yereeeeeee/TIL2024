'''
곰곰이와 자판기

M번 차원이동을 하고,
음료수 종류 U는 V로 바뀐다.
'''
import sys; input = sys.stdin.readline
N,M = map(int,input().split())
stack = [tuple(map(int,input().split())) for _ in range(M)]
ans = [*range(N+1)]
for u,v in stack[::-1]: ans[u]=ans[v]
print(*ans[1:])