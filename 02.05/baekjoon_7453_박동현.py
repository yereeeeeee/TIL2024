'''
합이 0인 네 정수

MTIM, 투 포인터

완전 동일한 로직으로,

python 시간 초과
pypy 689172kb, 6968ms
go 255836kb, 7528ms

go가 지는 경우 처음봄; 근데 go가 메모리 효율은 압도적.
'''
import sys; input = sys.stdin.readline


def find(arr, idx):
    target = arr[idx]
    res = 0
    for i in range(idx, N*N):
        if target == arr[i]:
            res += 1
        else: break
    return res

N = int(input())
A,B,C,D = [], [], [], []

for _ in range(N):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

AB.sort(); CD.sort(reverse=True)

ab, cd = 0, 0
ans = 0
while cd < N*N and ab < N*N:
    total = AB[ab] + CD[cd]
    if total == 0:
        ab_cnt = find(AB, ab)
        cd_cnt = find(CD, cd)
        ans += ab_cnt * cd_cnt
        ab += ab_cnt
        cd += cd_cnt
    elif total > 0: cd += find(CD, cd)
    else: ab += find(AB, ab)

print(ans)