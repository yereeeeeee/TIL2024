from heapq import heappop, heappush


N,M = map(int,input().split())
arr = sorted([*map(int,input().split())], reverse=True)
hq = [0] * M

ans = 0
for a in arr:
    ans = max(ans, (tmp:=heappop(hq) + a))
    heappush(hq, tmp)

print(ans)
