'''
두 수 XOR

트라이

두 수를 XOR 한 값 중 가장 큰 값을 찾으면 된다.
테케가 작아 단순 순회로 문제를 해결할 수도 있지만, 트라이를 사용할 수 있으니 트라이를 사용했다.


* 단순한 순회 방식은, 가장 큰 값을 찾고, 이진수로 만들어 0이 처음 시작하는 시점과 같거나 그보다 작은 수부터 순회하면 된다.
'''


def make_bin(num):
    tmp = bin(num)[2:]
    return (max_length-len(tmp))*"0" + tmp    


def insert(num):
    binary = make_bin(num)

    now = trie
    for b in binary:
        now = now.setdefault(int(b), dict())


def compare(num):
    now = trie

    binary = make_bin(num)
    res = ""
    for b in binary:

        check = 1-int(b)
        
        if check in now:
            res+= "1"
            now = now[check]

        else:
            res+= "0"
            now = now[1-int(check)]
    
    return int(res,2)


trie = dict()

N = int(input())
arr = sorted([*map(int,input().split())], reverse=True)

# 최대 길이를 구함
max_length = len(bin(arr[0]))-2

for num in arr:
    insert(num)

ans = 0
for num in arr:
    ans = max(ans, compare(num))

print(ans)