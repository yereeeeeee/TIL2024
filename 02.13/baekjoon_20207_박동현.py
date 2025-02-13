'''
누적합 그리디 풀이
'''
import sys; input = sys.stdin.readline


N = int(input())
day = [0] * 367

for _ in range(N):
    s,e = map(int,input().split())
    day[s] += 1
    day[e+1] -= 1

for i in range(1,367):
    day[i] += day[i-1]

ans = 0
height, width = 0,0
for i in range(1,367):
    if day[i]:
        width += 1
        height = max(height, day[i])
    else:
        ans += width * height
        height, width = 0,0

print(ans)

'''
스위핑 풀이
'''
import sys; input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    s,e = map(int,input().split())
    arr.append((s, -1))
    arr.append((e, +1))

arr.sort()

ans = 0
cnt = 0
left,right,height = float('inf'),0,0

for i in range(N*2):
    k,w = arr[i]

    cnt -= w
    height = max(cnt, height)

    if w == -1:
        left = min(left, k)
    else:
        right = max(right, k)
    
    if cnt == 0:
        if i < 2*N-1 and k+1 == arr[i+1][0]: continue

        ans += height * (right-left+1)
        left,right,height = float('inf'),0,0

print(ans)