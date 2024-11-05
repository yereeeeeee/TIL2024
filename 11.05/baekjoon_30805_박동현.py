'''
사전 순 최대 공통 부분 수열

enumerate로 역순 정렬한 후 인덱스를 저장해가며 가져갈 수 있으면 가져간다.
'''


N = int(input())
arr = sorted(enumerate([*map(int,input().split())]), key=lambda x: -x[1])

M = int(input())
brr = sorted(enumerate([*map(int,input().split())]), key=lambda x: -x[1])
# 인덱스
a,b = 0,0
ans = []
a_check,b_check = -1,-1
while N > a and M > b:
    if arr[a][0] < a_check:
        a += 1
        continue
    if brr[b][0] < b_check:
        b += 1
        continue

    if arr[a][1] == brr[b][1]:
        if arr[a][0] > a_check and brr[b][0] > b_check:
            ans.append(arr[a][1])
            a_check = arr[a][0]
            b_check = brr[b][0]
            a += 1
            b += 1

    elif arr[a][1] > brr[b][1]:
        a += 1
    else :
        b += 1

print(len(ans))
print(*ans)
