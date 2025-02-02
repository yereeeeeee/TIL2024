if (S:=input())[0] == "0": exit(print(0))
length = len(S)
S = "0" + S

DP = [0] * (length+1)
DP[0] = DP[1] = 1
for i in range(2,length+1):
    if int(S[i]):
        DP[i] += DP[i-1]

    if 10 <= int(S[i-1:i+1]) <= 26:
        DP[i] += DP[i-2]

    DP[i] %= 1000000
print(DP[-1])