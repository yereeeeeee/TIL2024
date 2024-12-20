'''
반도체 설계

DP, nlogn

재활문제
'''

def bs(num):
    start,end = 0,len(DP)-1

    while start <= end:
        mid = (start+end) // 2

        if DP[mid] == num: return mid
        elif DP[mid] < num: start = mid + 1
        else: end = mid - 1
    return mid

N = int(input())
arr = [*map(int,input().split())]

DP = [arr[0]]

for item in arr:
    if DP[-1] < item:
        DP.append(item)
    else:
        DP[bs(item)] = item

print(len(DP))