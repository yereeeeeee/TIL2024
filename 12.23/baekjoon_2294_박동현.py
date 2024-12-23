'''
동전 2

DP

DP재활
'''
import sys; input = sys.stdin.readline


N,K = map(int,input().split())

arr = [int(input()) for _ in range(N)]
DP = [float('inf')]*(K+1)
DP[0] = 0
for i in range(N):
    for j in range(K+1):
        if arr[i] > j: continue
        DP[j] = min(DP[j], DP[j-arr[i]]+1)

print(DP[-1] if DP[-1] != float('inf') else -1)