import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

first = []
second = []
for i in range(n):
    for j in range(n):
        first.append(arr[i][0] + arr[j][1])
        second.append(arr[i][2] + arr[j][3])

first.sort()
second.sort()

answer = 0

start = 0
end = len(second) - 1

while start < len(first) and end >= 0:

    target = first[start] + second[end]

    if target > 0:
        end -= 1
    elif target < 0:
        start += 1

    else:
        next_start = start + 1
        next_end = end - 1

        while next_start < len(first) and first[start] == first[next_start]:
            next_start += 1
        while next_end >= 0 and second[end] == second[next_end]:
            next_end -= 1

        answer += (next_start - start) * (end - next_end)
        start, end = next_start, next_end

print(answer)