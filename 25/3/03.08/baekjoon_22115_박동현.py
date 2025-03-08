N,K = map(int,input().split())
DP = [0]+[float('inf')]*K
coffees = [*map(int,input().split())]
for coffee in coffees:
    for i in range(K-1, -1, -1):
        if i + coffee > K: continue
        DP[i+coffee] = min(DP[i+coffee], DP[i] + 1)
print(DP[K] if DP[K] != float('inf') else -1)