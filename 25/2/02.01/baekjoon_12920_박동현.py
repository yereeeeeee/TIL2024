'''
평범한 배낭 2

배낭 문제, 단조 큐를 통한 최적화

단조 큐는 DP에서 슬라이딩 윈도우처럼 작동한다.
상태 전이 과정에서 불필요한 탐색을 줄이고, 최적 상태만 남겨 효율적으로 DP계산을 수행한다.

이 문제에서는 각 아이템에 대해 최대 K번 사용이 가능하다.
단조 큐를 활용하여 각 상태에서 최적 전이를 효율적으로 관리한다.
'''
import sys; input = sys.stdin.readline
from collections import deque


N,M = map(int,input().split())

DP = [0] * (M+1)
for _ in range(N):
    V,C,K = map(int,input().split())

    for i in range(V):
        weight = i
        
        q = deque()
        q.append((DP[i], 0))

        max_jump = (M-i) // V
        for jump in range(1, max_jump + 1):
            weight += V
            
            if jump - q[0][1] > K:
                q.popleft()

            tmp = DP[weight] - jump*C
            while q and tmp > q[-1][0]:
                q.pop()
            
            q.append((tmp, jump))
            DP[weight] = q[0][0] + jump*C

print(DP[M])

'''
기존 풀이

"2의 지수로 모든 숫자를 표현할 수 있다." 라는 명제에서 시작한다.
2의 지수 단위로 아이템을 분할해 기존 0/1 배낭 문제처럼 해결할 수 있다.

ex) 6 = 1+2+3, 15 = 1+2+4+8
왜 지수라면서 3이 담기나요? -> 1,2,4,8 단위로 분할하는데, 
남은 값이 지수보다 작으면 나머지가 담긴다.

이렇게 수행하는 경우 6번 반복 -> 3번 반복, 15번 반복 -> 4번 반복으로 
분할 정복과 같은 최적화 효과를 갖는다.
'''
import sys; input = sys.stdin.readline


N,M = map(int,input().split())
arr = []
for _ in range(N):
    V,C,K = map(int,input().split())

    idx = 1
    while K:
        tmp = min(idx, K)
        arr.append((V*tmp, C*tmp))
        idx *= 2
        K -= tmp

DP = [0] * (M+1)
for v,c in arr:
    for j in range(M, v-1, -1):
        DP[j] = max(DP[j], DP[j-v] + c)
print(DP[M])