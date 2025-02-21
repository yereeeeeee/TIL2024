'''
개똥벌레

이분탐색

홀짝 인덱스를 나눠서 이분탐색
'''
import sys; input = sys.stdin.readline


def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] <= num:
            start = mid + 1
        else:
            end = mid - 1 
    return start


N,H = map(int,input().split())

up, down = [], []
for i in range(N):
    if i % 2 :
        up.append(int(input()))
    else:
        down.append(int(input()))

down.sort()
up.sort()

min_v = N
min_c = 0
for i in range(1, H+1):
    down_cnt = len(down) - binary_search(down, i - 0.5)
    up_cnt = len(up) - binary_search(up, H - i + 0.5)
    
    total_cnt = down_cnt + up_cnt

    if min_v == total_cnt:
        min_c += 1
    elif min_v > total_cnt:
        min_c = 1
        min_v = total_cnt
print(min_v, min_c)