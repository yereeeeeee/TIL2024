'''
겨울이 좋아

이분 탐색

n일 만에, 마법을 n번 이내로 쓰고, 나뭇잎이 다 떨어지게 만들 수 있는가?
'''
from math import ceil 


def is_winter(day):
    res = [*map(lambda x: max(0, x-day), arr)]
    return sum(res) <= day

N = int(input())
arr = [ceil(i[0]/i[1]) for i in zip(map(int,input().split()), map(int,input().split()))]

left, right = 0, max(arr)

while left <= right:
    mid = (left+right) // 2
    if is_winter(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)