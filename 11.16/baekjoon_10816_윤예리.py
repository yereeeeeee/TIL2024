import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))

nums = {}
for i in range(n):
    if arr[i] in nums:
        nums[arr[i]] += 1
    else:
        nums[arr[i]] = 1

for i in range(m):
    if find[i] in nums:
        print(nums[find[i]], end=" ")
    else:
        print(0, end=" ")
