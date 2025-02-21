'''
제곱근 수열

DP

1. 제한은 최대 7만이고, 6번까지 가는게 최대임 그 이상은 무조건 0이라
    - 파이썬 기준 제한하면 68ms 제한 안하면 3500ms
'''

for _ in range(int(input())):
    N,M = map(int,input().split())
    if M>=6: print(0); continue
    
    DP = [[0]*(N+1) for _ in range(M)]
    DP[0][N] = 1
    for i in range(M-1):
        for j in range(N, 1, -1):
            if DP[i][j]:
                
                for k in range(1, int((j-1)**0.5)+1):
                    DP[i+1][k] += DP[i][j]
    print(DP[M-1][1])