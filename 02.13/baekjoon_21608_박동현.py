import sys; input = sys.stdin.readline


def find_position(num):
    max_v = 0
    result = []
    for x in range(N):
        for y in range(N):
            if arr[x][y]: continue
            tmp = get_count(x,y, num)
            if tmp > max_v:
                max_v = tmp
                result = [(x,y)]
            elif tmp == max_v:
                result.append((x,y))
    
    max_v = -1
    for x,y in result:
        tmp = 0
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                tmp += arr[nx][ny] == 0
        if tmp > max_v:
            max_v = tmp
            rx,ry = x,y

    return rx,ry

def get_count(x,y, key):
    res = 0
    for dx,dy in dr:
        nx,ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            res += arr[nx][ny] in data[key]
    return res

dr = (1,0),(0,1),(-1,0),(0,-1)

N = int(input())
data = {key: set(value) for _ in range(N**2) for key, *value in [map(int,input().split())]}

arr = [[0]*N for _ in range(N)]
for key in data:
    x,y = find_position(key)
    arr[x][y] = key

ans = 0
for i in range(N):
    for j in range(N):
        ans += int(10**(get_count(i,j, arr[i][j])-1))
print(ans)