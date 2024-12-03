'''
본대 산책 2

분할 정복, 행렬 제곱

정보과학관: 0
전산관: 1
미래관: 2
신양관: 3
한경직기념관: 4
진리관: 5
학생회관: 6
형남공학관: 7

최대 10억번 움직이게 되는데, 이걸 DP로 구하기는 어렵다
그래서 분할 정복을 사용해서, 행렬 제곱을 활용해 가능한 가지수를 구할 수 있다.
간단히 인접 리스트를 만들고, 이걸 곱하면 된다.
'''
def multiply(now, fr=0, to=0):
    if now <= 1:
        return maps[now][fr][to]
    
    maps.setdefault(now, [[0]*8 for _ in range(8)])
    if maps[now][fr][to]: return maps[now][fr][to]

    nxt_even = now // 2
    nxt_odd = nxt_even + 1 if now % 2 else nxt_even

    for i in range(8):
        maps[now][fr][to] += multiply(nxt_even, fr, i) * multiply(nxt_odd, i, to)
        maps[now][fr][to] %= 1000000007
    return maps[now][fr][to]
    
maps = dict()
maps[1] = [
    [0,1,1,0,0,0,0,0],
    [1,0,1,1,0,0,0,0],
    [1,1,0,1,1,0,0,0],
    [0,1,1,0,1,1,0,0],
    [0,0,1,1,0,1,0,1],
    [0,0,0,1,1,0,1,0],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,1,0,1,0]
]

print(multiply(int(input())))