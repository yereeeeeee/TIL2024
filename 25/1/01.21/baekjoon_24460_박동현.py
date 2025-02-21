import sys; input = sys.stdin.readline


def div_conq(size, x=0, y=0):
    if next_size:=size//2:
        res = []
        for i in 0, next_size:
            for j in 0, next_size:
                res.append(div_conq(next_size, x+i, y+j))
        return sorted(res)[1]
    return arr[x][y]

N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]

print(div_conq(N))