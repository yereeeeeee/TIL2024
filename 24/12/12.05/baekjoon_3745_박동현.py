'''
오름세

nlogn lis
'''

import sys; input = sys.stdin.readline


def lis(num):
    left, right = 0, len(DP)
    
    while left <= right:
        mid = (left+right) // 2
        if DP[mid] > num:
            right = mid-1
        elif DP[mid] == num: 
            return mid
        else:
            left = mid+1
    return left

while True:
    try:
        N = int(input())
        arr = [*map(int,input().split())]

        ans = 0
        DP = []
        for i in arr:
            if not DP or DP[-1] < i:
                DP.append(i)
            else:
                DP[lis(i)] = i
        print(len(DP))
    except:
        break