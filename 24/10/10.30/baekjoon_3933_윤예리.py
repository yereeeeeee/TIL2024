# dp에 미리 가능한 경우의 수를 저장해놓음
max_n = (1 << 15)
# dp[i][j] = j개의 제곱수 합으로 i를 표현할 수 있는 경우의 수
dp = [[0] * 5 for _ in range(max_n)]

for i in range(1, int(max_n ** 0.5)+1):
    tmp = i*i
    dp[tmp][1] = 1

    for j in range(tmp, max_n):
        for k in range(2, 5):
            dp[j][k] += dp[j-tmp][k-1]

while True:
    n = int(input())
    if n == 0:
        break

    answer = sum(dp[n][k] for k in range(1, 5))
    print(answer)

# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     arr = arr = [i**2 for i in range(1, int(n**0.5) + 1)]
#     answer = 0
#     k = len(arr)
#
#     for start in range(k):
#         total = 0
#         for end in range(start, k):
#             total += arr[end]
#
#             if total == n:
#                 answer += 1
#             elif total > n:
#                 break
#
#     print(answer)