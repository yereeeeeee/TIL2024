import sys; input = sys.stdin.readline


def dfs(x,y,now,nxt):
    if before[x][y] != now: return
    before[x][y] = nxt
    for dx,dy in dr:
        nx,ny = x+dx, y+dy
        if 0 <=nx < N and 0 <= ny < M:
            dfs(nx,ny,now,nxt)

def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if before[i][j] != after[i][j]:
                dfs(i,j, before[i][j], after[i][j])
                cnt += 1
                if cnt > 1: return False
    return True

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
before = [[*map(int,input().split())] for _ in range(N)]
after = [[*map(int,input().split())] for _ in range(N)]

print("YES" if check() and before==after else "NO")