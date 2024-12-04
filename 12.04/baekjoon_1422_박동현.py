'''
숫자의 신

정렬, 그리디

비슷한 정렬방식의 문제가 생각나서 그거 기반으로 하고, 숏코딩이나 한번 해봤음

* lambda x: x*10 으로 정렬이 되는 이유

파이썬의 문자열 정렬 로직은
맨 앞에서부터 차례대로, ascii 순 -> 길이 순 으로 비교한다.
그래서 arr = ['1', '11', '10', '101'] 을 정렬하면
숫자 기준이 아니라 위의 문자열 비교방식 기준으로 ['1','10','101','11'] 을 출력한다.

그렇기 때문에, 최대 10억인 숫자를 기준으로하기 때문에 모두 최소 10자리를 채워 버리면 
10자리 내에서 반복을 가정해서 모두 비교할 수 있고, 문제가 원하는 답을 도출할 수 잇다.
'''

N,M=map(int,input().split())
l=[input().strip()for _ in range(N)]
for _ in range(M-N):l.append(str(max(map(int,l))))
print(*sorted(l,key=lambda x:x*10)[::-1],sep="")



'''
별 차이 없긴 함

N,M = map(int,input().split())
arr = [input().strip() for _ in range(N)]
for _ in range(M-N):
    arr.append(str(max(map(int,arr))))
print(*sorted(arr, key=lambda x: x*10)[::-1], sep="")
'''