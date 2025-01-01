'''
문자열 변환과 쿼리

문자열, 해시맵

철자의 참조를 딕셔너리에 저장해두고, 
업데이트가 있을 때마다 순회하며 참조값이 해당 값인 경우 변환한다.
'''
import sys; 
input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(x)


def change(now, nxt):
    global res
    for k,v in data.items():
        if v == now:
            data[k] = nxt
    res = ""

def sout():
    global res
    if not res:
        res = "".join(data[char] for char in word)
    answer.append(res)


query = {
    "1": change,
    "2": sout
}

data = {chr(a): chr(a) for a in range(65, 123)}

S,N = input().split()
word = list(S)
res = ""
answer = []
for _ in range(int(N)):
    a, *b = input().split()
    query[a](*b)

print("\n".join(answer))
