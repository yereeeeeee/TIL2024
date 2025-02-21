'''
기타 레슨

순서는 바뀌면 안되고,
총 합에서 M을 나눈 값을 기준으로 한칸씩 올려가면서 계산

이분 탐색
'''

N,M = map(int,input().split())
arr = [*map(int,input().split())]

total = sum(arr)
left = total//(M+1)
right = M * 10000
ans = 0 
while left < right:
    mid = (left+right) // 2
    cnt = 1
    tmp = 0
    for i in range(N):
        if tmp+arr[i]<=mid:
            tmp += arr[i]
        elif mid < arr[i]:
            cnt = M+1
            break
        else:
            tmp = arr[i]
            cnt += 1
            if cnt > M:
                break

    if cnt <= M:
        ans = mid
        right = mid
    elif cnt > M:
        left = mid+1

print(ans)