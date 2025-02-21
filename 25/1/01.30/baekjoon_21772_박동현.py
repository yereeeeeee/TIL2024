'''
가희의 고구마 먹방

백트래킹

논리적으로 dfs랑 크게 다를바는 없어보임
특정 결과값을 찾는 것이 아니라 모든 경로를 탐색해야 하고
그 과정에서 가지치기가 유용할 것이라 판단해 백트래킹 분류가 맞다고 생각했음
'''
import sys; input = lambda: sys.stdin.readline().strip()


def find(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                return i,j

def backtrack(x, y, idx=0, result=set()):
    global ans
    if idx == K:
        ans = max(ans, len(result))
        return

    if len(result) + (K - idx) <= ans:
        return

    for dx,dy in dr:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == "#": continue
            backtrack(nx, ny, idx+1, result | {(nx,ny)} if arr[nx][ny] == "S" else result)

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M,K = map(int,input().split())
arr = [input() for _ in range(N)]

ans = 0
backtrack(*find("G"))
print(ans)