import sys; input = sys.stdin.readline


def lawning(dx,dy, x,y):
    global lawn
    x -= 1
    y -= 1
    while arr[x][y]:
        arr[x][y] = 0
        lawn -= 1
        x += dx
        y += dy
        if not (0<=x<N and 0<=y<M): return

def check(x,y):
    print(1-arr[x-1][y-1])

def cnt():
    print(lawn)

cmd = {
    1: lawning,
    2: check,
    3: cnt
}


N,M,Q = map(int,input().split())
arr = [[1]*N for _ in range(M)]
lawn = N*M

for _ in range(Q):
    q, *query = map(int,input().split())
    cmd[q](*query)