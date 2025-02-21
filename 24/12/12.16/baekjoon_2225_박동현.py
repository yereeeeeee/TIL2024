'''
합분해

DP

DP 재활훈련
'''

N,K = map(int,input().split())
DP = [[0]*(K+1) for _ in range(N+1)]
DP[0][0] = 1
for i in range(N+1):
    for j in range(1,K+1):
        DP[i][j] = (DP[i-1][j]+DP[i][j-1]) % 1000000000
print(DP[-1][-1])
