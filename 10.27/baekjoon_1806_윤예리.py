import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
total = 0
answer = 1e9

while True:
    # 넘으면 길이 비교해서 정답 갱신하고 제일 왼쪽 숫자 빼봄
    if total >= s:
        answer = min(answer, end-start)
        total -= arr[start]
        start += 1

    elif end == n: break

    # 아니면 오른쪽 total에 더해주고
    else:
        total += arr[end]
        end += 1

if answer == 1e9: print(0)
else: print(answer)