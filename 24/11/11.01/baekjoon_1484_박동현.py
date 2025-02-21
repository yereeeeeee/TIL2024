'''
다이어트, 투포인터
start와 end가 N만큼 차이나는 값을 찾으면 ans 에 넣고, 아니면 차이에 따라 조절한다.
'''
N = int(input())

start,end = 1,2 
ans = []
while start < end:
    if end**2 - start**2 == N:
        # 정답인 경우 ans에
        ans.append(end)
        start += 1 
        end += 1

    elif end**2 - start**2 < N:
        end += 1

    else :
        start += 1
# ans 리스트가 하나라도 있는 경우 전체 출력
if ans:
    print(*ans, sep="\n")
# 아니면 -1 출력
else:
    print(-1)