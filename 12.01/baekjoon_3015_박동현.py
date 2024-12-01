'''
오아시스 재결합

스택

스택을 쓰는데, 튜플에 카운트를 저장해서 사용
'''



import sys; input = sys.stdin.readline


arr = [int(input()) for _ in range(int(input()))]

stack = []
ans = 0

for i in arr:
    while stack and stack[-1][0] < i:
        ans += stack.pop()[1]

    if not stack:
        stack.append((i, 1))
    
    elif stack[-1][0] >= i:

        if stack[-1][0] == i:
            cnt = stack.pop()[1]
            ans += cnt

            if stack:
                ans += 1
            stack.append((i, cnt+1))

        else:
            stack.append((i, 1))
            ans += 1

print(ans)