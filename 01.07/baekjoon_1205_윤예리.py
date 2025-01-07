import sys
input = sys.stdin.readline

n, new, p = map(int, input().split())

if n == 0:
    print(1)  # 리스트가 없으면 1등
    exit()

arr = sorted(list(map(int, input().split())), reverse=True)
answer = 1

for i in range(n):
    if arr[i] > new:
        answer += 1  # 등수 증가
    elif arr[i] == new:
        pass  # 동일 점수는 순위 유지
    else:
        break  # 더 작은 점수면 종료

# p개를 초과하거나, 마지막 순위에서 new가 포함되지 못하는 경우 처리
if answer > p or (n == p and new <= arr[-1]):
    print(-1)
else:
    print(answer)
