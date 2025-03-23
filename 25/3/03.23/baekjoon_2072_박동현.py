'''
(1,1) - (19,19)
수를 둘 때마다 관리하기
'''
def check(x,y):
    check = arr[x][y]
    drx = ((1,0),(-1,0)),((0,1),(0,-1)),((-1,1),(1,-1)),((1,1),(-1,-1))
    for dr in drx:
        res = 1
        for dx,dy in dr:
            nx,ny = x+dx,y+dy
            while 0 < nx < 20 and 0 < ny < 20:
                if arr[nx][ny] != check: break
                res += 1
                nx += dx
                ny += dy
        if res == 5: return True

    return False

N = int(input())

ans = -1
arr = [[-1]*20 for _ in range(20)]
for k in range(1,N+1):
    x,y = map(int,input().split())

    arr[x][y] = k%2

    if ans == -1 and check(x,y):
        ans = k
print(ans)