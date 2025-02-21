'''
전깃줄 - 2

LIS, 역추적

#14003 '가장 긴 증가하는 부분 수열 5'의 전깃줄 버전
'''
import sys; input = sys.stdin.readline
from bisect import bisect_left

# def binary_search(num):
#     left, right = 0, len(LIS)-1
#     while left <= right:
#         mid = (left+right) // 2
#         if LIS[mid] == num: return mid
#         if LIS[mid] < num:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left

N = int(input())
arr = sorted([[*map(int,input().split())] for _ in range(N)])

LIS = [arr[0][1]]
DP = []
for a,b in arr:
    if LIS[-1] < b:
        LIS.append(b)
        DP.append(len(LIS))
    else:
        # nxt = binary_search(b)
        nxt = bisect_left(LIS, b)
        LIS[nxt] = b
        DP.append(nxt+1)


length = len(LIS)
ans = []
for i in range(N-1, -1, -1):
    if length == DP[i]: length -= 1; continue
    ans.append(arr[i][0])
    
print(len(ans))
print(*ans[::-1], sep="\n")
