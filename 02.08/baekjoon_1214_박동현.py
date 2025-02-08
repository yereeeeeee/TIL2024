def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def lcm(a,b):
    return a * b // gcd(a,b)

D,P,Q = map(int,input().split())

if P < Q: 
    P,Q = Q,P

ans = float('inf')

for i in range(0, min(D,lcm(P,Q))+P, P):
    target = max(D-i, 0)
    tmp = target // Q * Q

    if tmp < target:
        tmp += Q
    ans = min(ans, tmp+i)
print(ans)