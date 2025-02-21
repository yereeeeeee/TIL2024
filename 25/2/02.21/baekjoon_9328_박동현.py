'''
열쇠

BFS

패딩을 씌우고, (0,0)에서 시작
# 1. 열쇠를 사용할 수 있는 방에 도달한다.
# 2. 안에 물건을 찾는다 (만약 달러라면, 원본 배열을 "." 으로 만들고, ans를 증가시킨다.)
# 3. 안에 물건이 열쇠라면, 열쇠배열에 추가해 새로이 dfs를 진행한다.
'''
import sys; input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**5)


dr = (1,0),(0,1),(-1,0),(0,-1)

def dfs(x,y, key):
    stack = [(x,y)]
    visit = [[False]*M for _ in range(N)]
    check = False
    while stack:
        x,y = stack.pop()

        if visit[x][y]: continue

        visit[x][y] = True

        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny].isupper() and arr[nx][ny].lower() not in key: continue
                
                if arr[nx][ny] == "*": continue
                
                if arr[nx][ny] == "$":
                    arr[nx][ny] = "."
                    global ans
                    ans += 1
                    
                if arr[nx][ny].islower():
                    tmp = arr[nx][ny]
                    arr[nx][ny] = "."
                    key += tmp
                    check = True
                    
                stack.append((nx,ny))
    if check: dfs(0,0,key)

for _ in range(int(input())):

    N,M = map(int,input().split())

    arr = []
    arr.append(list("."*(M+2)))
    for _ in range(N):
        arr.append(list("." + input() + "."))
    arr.append(list("."*(M+2)))
    
    N+=2
    M+=2
    key = input()
    ans = 0
    dfs(0,0,key)
    print(ans)
