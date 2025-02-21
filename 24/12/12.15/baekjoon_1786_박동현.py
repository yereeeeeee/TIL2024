'''
찾기

kmp

1학기 때 배웠던 kmp는 백준에서 플레 문제다.
지금 다시 보니까 이해하기 좀 쉬움
'''

def create_kmp(word):
    res = [0]*len(s)

    j = 0
    for i in range(1,len(s)):
        while j > 0 and word[i] != word[j]:
            j = res[j-1]

        if word[i] == word[j]:
            j += 1
            res[i] = j
    return res

t = input()
s = input()
kmp = create_kmp(s)

#KMP 로직 돌리면 끝
answer = []
j = 0 
for i in range(len(t)):
    while j and t[i] != s[j]:
        j = kmp[j-1]
    if t[i] == s[j]:
        if j == len(s)-1:
            answer.append(i-len(s)+2)
            j = kmp[j]
        else:
            j += 1

print(len(answer))
print(*answer)