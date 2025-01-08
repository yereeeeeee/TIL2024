'''
순열의 순서

이분탐색

순진하게 permutations 를 쓰기엔 20!는 너무 크다.
1 2 3 4 5 .. 처럼 순서가 있는 수열이니 규칙이 존재한다.
factorial을 통해 규칙을 해석하고, 규칙에 맞는 정답을 도출한다.
'''
from math import ceil

def memo(f):
    cache = dict()
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

@memo
def factorial(num):
    return 1 if num <= 1 else num * factorial(num-1)

def find_permutation(K):
    numbers = [*range(1, N+1)]
    res = []
    for i in range(N-1, -1, -1):
        s = ceil(K / factorial(i)) - 1

        K -= factorial(i) * s
        res.append(numbers.pop(s))
    return print(*res)

def find_index(*permutation):
    i = N
    numbers = [*range(1, N+1)]

    res = 1
    for num in permutation:
        numbers.pop(idx:=numbers.index(num))
        res += idx * factorial(i:=i-1)
    
    return print(res)

cmd = {
    1: find_permutation,
    2: find_index
}

N = int(input())
q, *args = map(int,input().split())
cmd[q](*args)
