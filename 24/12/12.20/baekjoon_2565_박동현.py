'''
전깃줄

DP

LIS 응용..인데
그럼 전깃줄도 nlogn 풀이가 있나?
'''
N = int(input())
arr = sorted([[*map(int,input().split())] for _ in range(N)])

DP = [1]*N
for i in range(1,N):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            DP[i] = max(DP[i], DP[j]+1)
print(N-max(DP))