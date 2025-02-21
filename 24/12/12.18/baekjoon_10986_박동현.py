'''
나머지 합

누적합

누적합 공식을 쓰되, 나머지에 대한 처리를 통해 조합을 구성하여 답을 도출
나머지 공식을 어떻게 쓰는지 몰라서 참조함
'''
# N,M = map(int,input().split())
# arr = [*map(int,input().split())]

# PS = [[0]*N for _ in range(N)]

# # PS[i][j]: i부터 j까지의 합
# ans = 0
# for i in range(N):
#     tmp = arr[i]%M
#     PS[i][i] = tmp
#     ans += 1 if tmp == 0 else 0

# for i in range(1,N):
#     tmp = (PS[0][i-1] + arr[i])%M
#     PS[0][i] = tmp
#     ans += 1 if tmp == 0 else 0

# for i in range(1,N):
#     for j in range(i+1,N):
#         tmp = (PS[0][j] - PS[0][i-1])%M
#         PS[i][j] = tmp
#         ans += 1 if tmp == 0 else 0

# print(ans)

N,M = map(int,input().split())
arr = [*map(int,input().split())]

r = [0]*M
prefix_sum = 0
for i in range(N):
    prefix_sum += arr[i]
    r[prefix_sum % M] += 1

ans = r[0]

for i in range(M):
    ans += r[i] * (r[i]-1) // 2

print(ans)