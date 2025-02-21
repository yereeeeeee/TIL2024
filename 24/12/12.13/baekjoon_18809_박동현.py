'''
Gaaaaaaaaaarden

백트래킹, BFS

# 0: 호수
# 1: 배양액을 뿌릴 수 없는 땅 x
# 2: 배양액을 뿌릴 수 있는 땅 o

# 3: 초록색 배양액을 뿌린 땅
# 4: 빨간색 배양액을 뿌린 땅
# cnt 를 별도로 옆에 두어 같은 시간에 도착했다면 꽃을 피워주자.

안전하게 구현만 신경 쓰니까 시공간 복잡도가 다 터져버림
'''

import sys; input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)


dr = (1,0),(0,1),(-1,0),(0,-1)

def bfs(arr):
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 2:
                q.append((i,j,arr[i][j]))

    visit = [[0]*M for _ in range(N)]
    ans = 0
    while q:
        i,j, color = q.popleft()
        if visit[i][j] == -2: continue

        for dx,dy in dr:
            di,dj = i+dx, j+dy
            if 0<=di<N and 0<=dj<M:
                # 1) 일반적인 bfs 경우
                if 0 < arr[di][dj] < 3:
                    arr[di][dj] = color
                    visit[di][dj] = visit[i][j] + 1
                    q.append((di,dj,color))
                
                elif 7-arr[di][dj] == color and visit[di][dj] == visit[i][j] + 1:
                    arr[di][dj] = 5
                    visit[di][dj] = -2
                    ans += 1
    return ans

def backtrack(idx=0, green=0, red=0):
    global ans
    if green == G and red == R:        
        ans = max(ans, bfs([i[:] for i in arr]))
        return
    
    if idx == N*M:
        return
    
    i = idx % N
    j = idx // N

    if arr[i][j] == 2:
        if green < G:
            arr[i][j] = 3
            backtrack(idx+1, green+1, red)
        if red < R:
            arr[i][j] = 4
            backtrack(idx+1, green, red+1)
        arr[i][j] = 2
    backtrack(idx+1, green, red)


N,M,G,R = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]
ans = 0
backtrack()
print(ans)