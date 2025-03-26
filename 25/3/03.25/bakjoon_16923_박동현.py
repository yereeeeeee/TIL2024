def get_words(S):
    for char in range(len(S)-1,-1,-1):
        for i in range(max(ord(S[char]), 97),123):
            if data[chr(i)] == 0:
                S[char] = chr(i)
                return S
        data[S[char]] -= 1
        S = S[:char]
    return S

S = list(input())

data = {chr(i): 0 for i in range(97,123)}
for char in S:
    data[char] += 1
    
S.append(" ")
data[" "] = 1

ans = "".join(get_words(S))
print(ans if ans else -1)