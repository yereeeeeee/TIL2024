import sys; input = sys.stdin.readline


N,M = map(int,input().split())
arr = [*map(int,input().split())]
route = [sorted((arr[i], arr[i+1])) for i in range(M-1)]

prefix_sum = [0] * (N+1)
for s,e in route:
    prefix_sum[s] += 1
    prefix_sum[e] -= 1
for i in range(N):
    prefix_sum[i+1] += prefix_sum[i]

cost = [[*map(int,input().split())] for _ in range(N-1)]

ans = 0
for i in range(1,N):
    if not prefix_sum[i]: continue
    when_pay_cash = prefix_sum[i] * cost[i-1][0]
    when_pay_card = prefix_sum[i] * cost[i-1][1] + cost[i-1][2]

    ans += min(when_pay_cash, when_pay_card)
print(ans)
