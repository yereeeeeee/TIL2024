N = int(input())
arr = sorted([*enumerate(tmp:=[0]+[*map(int,input().split())])], key=lambda x: -x[1])
total_seat = sum(tmp)
required_seat = total_seat // 2

DP = [0] * (total_seat+1)
DP[0] = 1

ans = 0
for idx, nums in arr:
    for seat in range(required_seat, -1, -1):
        party = seat+nums
        if DP[seat] and not DP[party]:
            ans = max(ans, party)
            DP[party] = idx

answer = []
while ans and DP[ans]:
    answer.append(DP[ans])
    ans -= tmp[DP[ans]]

print(len(answer))
print(*answer)