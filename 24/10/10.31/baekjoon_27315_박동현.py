from heapq import heappush, heappop
import sys; input = sys.stdin.readline
from math import ceil


N, M = map(int, input().split())
# 전체 리스트
hq = []

for _ in range(N):
    # D: 아이디어 난이도
    # P: 구현 난이도
    # T: 데이터 존재 여부 (0/1)
    # E: 에디토리얼 존재 여부(0/1)
    D, P, T, E = map(int, input().split())
    # 데이터가 있으면, 틀렸습니다를 받지 않는다 (아이디어 난이도만 맞으면, 구현 난이도가 0이라고 보면 됨)
    if T: P = 0
    if E: heappush(hq, (ceil(D/2), P//2))
    else: heappush(hq, (D,P))

HD, HP = map(int,input().split())

# 아이디어 난이도 이하이면 무조건 풀 수 있기 떄문에, 풀 수 있는 문제를 따로 리스트에 담아서 사용한다.
# 풀 수 있는 친구 (구현 난이도만 추가)
qh = []

ans = 0
while M :
    # 문제를 보고, 풀 수 있으면 qh로 옮긴다. 
    while hq and HD >= hq[0][0]:
        heappush(qh, heappop(hq)[1])
    # 더 풀 문제가 없으면 끝
    if not qh : break
    # 풀 문제가 있으면, qh에서 꺼내서, ans에 틀린 횟수를 계산한다.
    P = heappop(qh)
    ans += max(P-HP, 0)

    HP += 1
    HD += 1
    M -= 1

print(-1 if M else ans)