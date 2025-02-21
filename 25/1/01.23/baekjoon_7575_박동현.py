'''
바이러스

kmp

패턴 매칭 알고리즘으로, 가능한 모든 패턴을 만들어 비교
이게 정해인 것 같은데, 꽤 비효율적이라 느껴짐
'''
import sys; input = sys.stdin.readline


def find_pattern(virus):
    for v in virus:
        if counter[v] < N: return
    pi_original = create_pi(virus)
    pi_reversed = create_pi(virus[::-1])
    
    for i in range(N-1):
        if not kmp(virus, arr[i], pi_original) and not kmp(virus[::-1],arr[i], pi_reversed):
            return False
    return True

def create_pi(word):
    pi = [0] * K

    i = 0
    for j in range(1,K):
        while i and word[i] != word[j]:
            i = pi[i-1]

        if word[i] == word[j]:
            i += 1
            pi[j] = i
    return pi

def kmp(word, target, pi):
    i = 0
    for j in range(len(target)):
        while i and word[i] != target[j]:
            i = pi[i-1]

        if word[i] == target[j]:
            if i == K-1:
                return True
            i += 1

def sol():
    for i in range(len(arr[-1]) - K + 1):
        if find_pattern(arr[-1][i:i+K]):
            return True
    return False

N,K = map(int,input().split())

arr = []
counter = [0]*10001

for _ in range(N):
    input()
    tmp = [*map(int,input().split())]
    arr.append(tmp)

    for t in set(tmp):
        counter[t] += 1

print("YES" if sol() else "NO")