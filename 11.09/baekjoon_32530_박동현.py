'''
래환이의 택시 타기 대작전

정렬 그리디
분류는 스위핑인데 스위핑을 쓸 수 있는지는 잘 모르겠음
'''


import sys;input=sys.stdin.readline


def parse_time(time):
    hh,mm = map(int,time.split(":"))
    return hh*60+mm
    
N = int(input())
arr = sorted([parse_time(input()) for _ in range(N)])


now = arr[0]        # 현재 택시 최초 탑승자
ans = 1             # 최종 택시 대수 (0번 손님 태우고 시작하니까 1대부터 시작)
tmp = 1             # 현재 택시 탑승 인원
for i in range(1,N):
    if tmp < 3 and arr[i] <= now + 10:
        tmp += 1    # 지금 타고 있는 사람이랑 같이 갈 수 있다면, 인원수만 추가
    else:           # 같이 못가면 인원수 초기화 후 택시 대수 up
        tmp = 1
        ans += 1
        now = arr[i]

print(ans)