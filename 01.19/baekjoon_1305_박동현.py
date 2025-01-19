'''
광고

kmp

kmp 배열을 만들면, 마지막 값은 문자열에서 가장 긴 접두사와 접미사의 길이를 나타낸다.
즉, 반복되는 부분을 제거하면 문제에서 원하는 값을 도출할 수 있다.

-
'aaba'가 'aabaaa'로 반복되는 것은 이해하기 쉽지만, 'baaaba'처럼 반복하는 경우 문제를 이해하기 어려울 수 있다.
이 때, 'aaba'를 고정해서 생각하지 말고, 'baaa' 를 패턴이라 간주하면 쉽게 해결할 수 있다. 
'''

def create_kmp(word):
    kmp = [0]*N

    i = 0
    for j in range(1, N):
        while i and word[i] != word[j]:
            i = kmp[i-1]

        if word[i] == word[j]:
            i += 1
            kmp[j] = i

    return kmp


N = int(input())
kmp = create_kmp(input())
print(N - kmp[-1])
