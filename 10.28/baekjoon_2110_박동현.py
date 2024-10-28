'''
공유기 설치 골4 이분탐색
이분탐색 싫어

공유기 사이의 거리를 이분탐색을 통해 찾아나간다.
가능한 거리의 최대값과 최소값에서 available 함수에 맞는 경우 저장하면서 점점 좁혀나가는 방식
'''

import sys; input = sys.stdin.readline


def is_available(length):
    cur = arr[0]
    cnt = 1
    for i in range(1,N):
        if arr[i] >= cur+length:
            cnt += 1
            cur = arr[i]
    
    return cnt >= M
    

N,M = map(int,input().split())
arr = sorted([int(input()) for _ in range(N)])

start = 1
end = arr[-1] - arr[0]


ans = 0
while start <= end:
    mid = (start+end) // 2
    if is_available(mid):
        start = mid+1
        ans = mid
    else:
        end = mid-1

print(ans)