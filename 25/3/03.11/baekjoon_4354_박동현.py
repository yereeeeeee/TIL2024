import sys; input = lambda: sys.stdin.readline().strip()


def get_pi(word):
    length = len(word)
    pi = [0] * length

    i = 0
    for j in range(1, length):
        while i and word[i] != word[j]:
            i = pi[i-1]
        if word[i] == word[j]:
            i += 1
            pi[j] = i
    return pi[-1]

def solve(word):
    length = len(word)
    matched_length = get_pi(word)
    if length % (length - matched_length) != 0:
        return 1
    else:
        return length // (length - matched_length)

while (S:=input()) != ".":
    print(solve(S))