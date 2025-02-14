def backtrack(arr, x=0, y=0, dir=-1, total=0):
    
    arr = [row[:] for row in arr]
    now = arr[x][y]
    total += now[0]
    dir = now[1]
    
    arr[x][y] = (-1,-1)
    for i in range(1,17): move(arr, i)
    arr[x][y] = (0,0)
    
    nx,ny = x,y
    dx,dy = dr[dir%8]
    while True:
        nx, ny = nx+dx, ny+dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if arr[nx][ny] not in not_fish:
                backtrack(arr, nx, ny, dir, total)
        else:
            global ans
            ans = max(ans, total)
            return
    

def move(arr,idx):
    for x in range(4):
        for y in range(4):
            now = arr[x][y]
            if now[0] == idx:
                for i in range(8):
                    dx,dy = dr[(arr[x][y][1]+i)%8]
                    nx,ny = x+dx, y+dy
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if arr[nx][ny] == (0,0) or arr[nx][ny] not in not_fish:
                            arr[x][y] = arr[x][y][0], (arr[x][y][1]+i)%8
                            arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]
                            return

not_fish = (0,0),(-1,-1)
dr = (-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)

arr = [[(idx, dir-1) for idx,dir in zip(*[iter(map(int,input().split()))]*2)] for _ in range(4)]

ans = 0
backtrack(arr)
print(ans)