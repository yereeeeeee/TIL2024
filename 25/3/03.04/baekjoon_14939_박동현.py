def light_off(x,y,arr):
    for dx,dy in dr:
        nx,ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            arr[nx][ny] = not arr[nx][ny]
    
def backtrack(bit, arr, x=0, cnt=0):
    global ans
    if cnt > ans: return
    if x == 10:
        if all(not x for x in arr[-1]): 
            ans = min(cnt, ans)
        return
    
    for y in range(N):

        if x == 0 and not (bit & 1<<y): continue
        if x and not arr[x-1][y]: continue
    
        cnt += 1
        light_off(x,y,arr)
    
    backtrack(bit, arr, x+1, cnt)
    
dr = (0,0),(1,0),(0,1),(-1,0),(0,-1)

N = 10
arr = [[False] * N for _ in range(N)]
for i in range(N):
    tmp = input()
    for j in range(N):
        arr[i][j] = tmp[j]=="O"

ans = 101
for bit in range(1<<N):
    backtrack(bit, [row[:] for row in arr])
print(ans)