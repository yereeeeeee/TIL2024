'''
Cubeditor

kmp, 문자열

모든 가능한 문자열에 대해 슬라이싱하며 kmp 배열을 만들고 최대값을 비교
문자열 길이가 5000 이라 n*n logn 해도 2500만+. 시간 내에 가능
'''
def create_kmp(word):
    kmp = [0]*len(word)
    j = 0
    for i in range(1,len(word)):
        while j and word[i] != word[j]:
            j = kmp[j-1]
        
        if word[i] == word[j]:
            j += 1
            kmp[i] = j
    return max(kmp)

ans = 0
for i in range(len(word:=input())):
    ans = max(ans, create_kmp(word[i:]))
print(ans)