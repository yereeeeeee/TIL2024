import sys; input = lambda: sys.stdin.readline().strip()


N,M = map(int,input().split())
data = dict()
for i in range(M):
    data[input()] = i

cnt = 0
for k,v in sorted(data.items(), key=lambda x: x[1]):
    if cnt == N: break
    print(k)
    cnt += 1
