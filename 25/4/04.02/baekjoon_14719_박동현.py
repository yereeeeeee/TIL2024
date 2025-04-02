import sys; input = sys.stdin.readline


N,M = map(int,input().split())
arr = [[0]*M for _ in range(N)]
for j,v in enumerate(map(int,input().split())):
    for i in range(v):
        arr[i][j] = 1

ans = 0
for i in range(N):
    tmp = 0
    check = False
    for j in range(M):
        if check and arr[i][j] == 0:
            tmp += 1
        if arr[i][j] == 1:
            check = True
            ans += tmp
            tmp = 0
print(ans)