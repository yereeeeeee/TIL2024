import sys; input = sys.stdin.readline


N,M = map(int,input().split())
arr = sorted([[*map(int,input().split())] for _ in range(N)], key=lambda x: (x[1],-x[0]))

ans = float('inf')
cnt = 1
now = -1
total = 0
for weight, cost in arr:
    total += weight

    if cost > ans: break
    if now == cost:
        cnt += 1
    else:
        cnt = 1
    now = cost

    if total >= M:
        ans = min(ans, cost * cnt)
print(-1 if ans == float('inf') else ans)