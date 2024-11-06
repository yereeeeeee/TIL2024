'''
계단수

DP는 DP인데, 일반적인 방식으로는 시간초과가 발생
풀이는 비트필드를 활용한 DP방식. 
'''

import sys;input = sys.stdin.readline


mod = 1000000000

N = int(input())
DP = [[dict() for _ in range(10)] for _ in range(N)]

# DP 마지막 딕셔너리에 1<<j (위치값) 저장
for j in range(1,10):
    DP[0][j][1 << j] = 1

# i: 자리수
# j: 숫자
# k: 위치값 (모든 숫자를 들러야하니까 이게 1111111111) 이 되면 완성
for i in range(N-1):
    for j in range(10):
        for k in DP[i][j]:
            v = DP[i][j][k]

            if j > 0:
                # 내려가는 파트
                # next를 설정하고 (저장된 위치값+지금 가려는 곳 (j-1))
                # 있으면 더하고, 아니면 딕셔너리에 추가
                next = k | (1 << (j-1))
                if next in DP[i+1][j-1]:
                    DP[i+1][j-1][next] += v
                    DP[i+1][j-1][next] %= mod
                else:
                    DP[i+1][j-1][next] = v
                
            if j < 9:
                # 올라가는 파트
                next = k | (1 << (j+1))
                if next in DP[i+1][j+1]:
                    DP[i+1][j+1][next] += v
                    DP[i+1][j+1][next] %= mod
                else:
                    DP[i+1][j+1][next] = v

# done = 1111111111  -> 다 들렀으면 res에 합산
done = (1 << 10) - 1
res = 0
for d in DP[-1]:
    res += d.get(done, 0)
        
print(res % mod)