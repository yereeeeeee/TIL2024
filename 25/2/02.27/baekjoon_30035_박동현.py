import sys; input = lambda: sys.stdin.readline().strip()
from math import ceil


def print_rank():

    if q[-1].isnumeric():
        tier, lv = q[:-1], int(q[-1])
        start, end = rank[tier]
        num = end-start+1
        if lv > num: return -1
        t = ceil(num / 4)
        
        return start + (t * (lv-1)) , min(end, start + (t*lv)-1)

    else:
        tier = q
        start, end = rank[tier]
        if end-start < 0: return -1
        return start,end

N,K = map(int,input().split())
rank = dict()

now = 1
for _ in range(K):
    tier, x = input().split()

    if "%" in x:
        p = int(x[:-1])
        num = (N-now + 1) * p // 100
    else: num = int(x)

    rank[tier] = (now, min(N,now+num-1))
    now = min(now + num, N+1)

q = input()

if now-1 != N: print("Invalid System")
else:
    ans = print_rank()
    if ans == -1:
        print("Liar")
    else:
        print(*ans)
