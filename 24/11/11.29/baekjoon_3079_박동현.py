'''
입국 심사

이분 탐색

조건을 통과하는 숫자를 이분 탐색을 통해 찾아낸다
최대가 10억 * 10억인데도 찾아지네요 신기합니다.
'''


import sys; input = sys.stdin.readline


def is_intime(time):
    ans = 0 
    for k in data:
        ans += (time // k) * data[k]
    return ans >= M

N,M = map(int,input().split())

data = dict()
for _ in range(N):
    a = int(input())
    data[a] = data.get(a,0)+1

left, right = 0, 1000000000*1000000000

while left <= right:
    mid = (left+right) // 2
    if is_intime(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)