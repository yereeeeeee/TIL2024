'''
평범한 배낭

DP, 배낭문제

배낭문제 재활훈련
예전엔 리스트로 구현했는데, 딕셔너리 형태가 훨씬 싸게 먹히는 것 같음.
'''

import sys; input = sys.stdin.readline


N,K = map(int,input().split())
DP = {0: 0}
arr = sorted([[*map(int,input().split())] for _ in range(N)], reverse=True)

for weight, value in arr:
    # DP를 순회하면서 추가해야 하는데, 이터레이션 대상인 데이터 구조를 루프 중에 수정하면 안된다.
    tmp = dict()
    for bag_value, bag_weight in DP.items():
        v = value+bag_value
        w = weight+bag_weight
        # DP(가방)에 있는 값, 없으면 최대치인 K가 w보다 작으면 스킵 
        if DP.get(v, K) < w: continue
        # 가방에 들어갈 수 있으면 tmp에 일단 저장
        tmp[v] = w
    # tmp에 저장된 값을 DP에 이관 
    DP.update(tmp)
print(max(DP))
