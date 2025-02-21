N = int(input())
answer = 0
enter, out = dict(), []
# 들어간 순서
for i in range(N):
    car = input()
    enter[car] = i
# 나오는 순서
for _ in range(N):
    car = input()
    out.append(car)

for i in range(N - 1):
    for j in range(i + 1, N):
        # 뒤에 있는 차가 먼저 나오면
        if enter[out[i]] > enter[out[j]]:
            answer += 1
            break
print(answer)