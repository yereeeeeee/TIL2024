'''
가장 긴 짝수 연속한 부분 수열 (large)

투 포인터

투 포인터 기본기.
'''


N,M = map(int,input().split())
arr = [*map(int,input().split())]

left,right = 0,0
cnt = int(arr[0] % 2)
ans = 0
while True:
    
    if cnt <= M or left==right:
        ans = max(ans, right-left-cnt+1)
        right += 1
    
        if right == N: break
        if arr[right] % 2: cnt += 1
    
    else:
        if arr[left] %2: cnt -= 1
        left += 1

print(ans)