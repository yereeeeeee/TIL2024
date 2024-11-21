'''
Fly me to the Alpha Centauri

수학으로 분류되어 있긴 한데, 이분 탐색으로 풀었음
'''
import sys; input = sys.stdin.readline
from math import ceil

# 1부터 num 까지 더하는 함수
def cal(num):
    if num <= 1: return num
    return ((num + 1) * num ) // 2

# (1 2 3 4 5) (4 3 2 1) 방식으로 더하는 함수
def teleport(num):
    return cal(num) + cal(num-1)


for _ in range(int(input())):

    N,M = map(int,input().split())
    length = M-N

    left,right = 0,2**31
    while left <= right:
        mid = (left+right) // 2
        if teleport(mid) == length:
            break
        elif teleport(mid) > length:
            right = mid-1
        else:
            left = mid+1

    # 1 2 3 4 5 (mid) // 4 3 2 1 (mid-1) // 이 길이에서는 최대 5가 2개 나올 수 있으니 남은 길이는 이에 맞춰 추가할 수 있음
    print(2*mid - 1 + ceil((length-teleport(mid)) / mid))