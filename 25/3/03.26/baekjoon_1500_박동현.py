N,K = map(int,input().split())
a,b = N//K, N%K
ans = 1
for _ in range(K):
    num = a
    if b:
        b -= 1
        num += 1
    ans *= num
print(ans)