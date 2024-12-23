'''
가장 긴 증가하는 부분 수열 5

LIS (N log N), 역추적

N log N 방식의 가장 큰 문제점은, 사용한 리스트의 길이는 맞으나 실제 값과 다를 수 있다는 점이다.
이를 해결하기 위해 별도의 배열을 두어 역추적이 가능하도록 설계했다.

그리고,
bisect의 시간복잡도가 압도적으로 빠르다.
단순한 방식으로 구현한 lis 함수보다 2배 이상 차이남

1. lis 구현 -> 163676kb, 2456ms
2. bisect 사용 -> 165712kb, 1172ms
'''

'''
1. lis 구현 방식
def lis(n):
    start,end = 0, len(ans)-1

    while start <= end:
        mid = (start+end) // 2

        if ans[mid] == n:
            return mid
        
        if ans[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

N = int(input())
arr = [*map(int,input().split())]

# 시작점을 기준으로
ans = [arr[0]]
DP = []
for item in arr:
    if ans[-1] < item:
        ans.append(item)
        DP.append(len(ans))
    else:
        nxt = lis(item)
        ans[nxt] = item
        DP.append(nxt+1)

x = len(ans)
tmp = float('inf')
res = []
for i in range(N-1, -1, -1):
    if x == DP[i] and tmp > arr[i]:
        res.append(arr[i])
        tmp = arr[i]
        x -= 1

print(len(ans))
print(*res[::-1])
'''

from bisect import bisect_left


N = int(input())
arr = [*map(int,input().split())]

ans = [arr[0]]
DP = []
for item in arr:
    if ans[-1] < item:
        ans.append(item)
        DP.append((len(ans)))
    else:
        nxt = bisect_left(ans,item)
        ans[nxt] = item
        DP.append(nxt+1)
    
x = len(ans)
tmp = float('inf')
res = []
for i in range(N-1, -1, -1):
    if x == DP[i] and tmp > arr[i]:
        res.append(arr[i])
        tmp = arr[i]
        x -= 1

print(len(ans))
print(*res[::-1])