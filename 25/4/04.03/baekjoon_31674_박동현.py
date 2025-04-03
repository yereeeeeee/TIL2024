mod = 10**9+7

N = int(input())
arr = sorted([*map(int,input().split())], reverse=True)

ans = 0
for a in arr: ans = (2 * ans + a) % mod
print(ans)