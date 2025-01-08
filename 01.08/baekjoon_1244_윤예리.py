import sys
input = sys.stdin.readline

# 스위치 개수
n = int(input())
# 스위치 상태
switches = list(map(int, input().split()))
# 학생 수
m = int(input())
# 학생 성별, 받은 수
students = [tuple(map(int, input().split())) for _ in range(m)]

# 토글 함수
def toggle(i):
    return abs(i-1)

for i in range(m):
    number = students[i][1]

    # 남자
    if students[i][0] == 1:
        for j in range(n):
            if not (j+1) % number:
                switches[j] = toggle(switches[j])

    # 여자
    else:
        k = 1
        mid = number - 1
        switches[mid] = toggle(switches[mid])
        while True:
            if mid - k < 0 or mid + k >= n:
                break

            if switches[mid-k] == switches[mid+k]:
                switches[mid-k] = toggle(switches[mid-k])
                switches[mid+k] = toggle(switches[mid+k])
                k += 1

            else:
                break

answer = [switches[i : i+20] for i in range(0, len(switches), 20)]
for i in range(len(answer)):
    print(*answer[i])