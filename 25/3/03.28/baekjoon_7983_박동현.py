import sys; input = sys.stdin.readline


now = float('inf')
for d,t in sorted([[*map(int,input().split())] for _ in range(int(input()))], key=lambda x: -x[1]): now = min(now, t) - d
print(now)