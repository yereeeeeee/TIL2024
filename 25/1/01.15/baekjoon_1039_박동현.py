'''
교환

탐색

그냥 자리수 교환하는 문제
'''
def search():
    next_stack = set()
    while stack:
        now = list(stack.pop())
        for i in range(length-1):
            for j in range(i+1, length):
                now[i],now[j] = now[j],now[i]
                if now[0] != "0": next_stack.add(tuple(now))
                now[i],now[j] = now[j],now[i]
    return list(next_stack)

def join(arr):
    return "".join(arr)

N,K = input().split()
length = len(N)
stack = [tuple(N)]

for _ in range(int(K)):
    if not stack: break
    stack = search()

print(-1 if not stack else max(map(join,stack)))