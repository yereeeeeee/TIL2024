'''
화학 제품

브루트 포스

백트래킹으로 죽어도 안풀리고, 진짜 말 그대로 브루트포스 하니까 풀림
'''


import sys; input=sys.stdin.readline


for _ in range(int(input())):

    A,B,C = map(int,input().split())
    AB,BC,CA = map(int,input().split())

    ans = -float('inf')
    for ab in range(min(A,B)+1):
        if BC>CA:
            bc = min(B-ab,C)
            res = AB*ab + BC*bc + CA*(min(C-bc, A-ab))
        else:
            ca = min(C,A-ab)
            res = AB*ab + CA*ca + BC*(min(B-ab, C-ca))
        ans = max(ans,res)
    
    print(ans)