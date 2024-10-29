'''
스타트 택시
구현 시뮬레이션 bfs A형 정석 문제
'''

import sys; input = sys.stdin.readline
from collections import deque
from heapq import heappop, heappush

# 시작 지점을 찾아야함
def find_start(a,b):
    # 현 위치
    q = deque([(a,b)])
    visit = [[0]*N for _ in range(N)]
    visit[a][b] = 1
    res = []
    check = False
    while q:
        x,y = q.popleft()

        if arr[x][y]:
            for i in arr[x][y]:
                if 0 < i < 1000:
                    heappush(res, (visit[x][y], x,y))
                    check = True
        if check: continue

        for dx,dy in dr:
            di,dj = x+dx, y+dy
            if 0<=di<N and 0<=dj<N and not visit[di][dj] and not board[di][dj]:
                q.append((di,dj))
                visit[di][dj] = visit[x][y] + 1
    
    # 시작지점에서 가장 가깝고, 행 렬이 가장 낮은 값을 찾음
    if res:
        _,i,j = res[0]
        for l in arr[i][j]:
            if 0 < l < 1000:
                arr[i][j].remove(l)
                return i,j, l, visit[i][j]-1
    # 없으면 -1 을 출력하고 종료
    return exit(print(-1))


# 목적지 찾기
def find_end(a,b,target):
    q = deque([(a,b)])
    visit = [[0]*N for _ in range(N)]
    visit[a][b] = 1

    while q:
        x,y = q.popleft()

        if arr[x][y]:
            for i in arr[x][y]:
                if i == target:
                    arr[x][y].remove(target)
                    return x,y,visit[x][y]-1

        for dx,dy in dr:
            di,dj = x+dx, y+dy
            if 0<=di<N and 0<=dj<N and not visit[di][dj] and not board[di][dj]:
                q.append((di,dj))
                visit[di][dj] = visit[x][y] + 1

    # 없으면 -1을 출력하고 종료
    return exit(print(-1))


dr = (-1,0),(0,-1),(1,0),(0,1)

N,M,K = map(int,input().split())        # N 격자, M 손님, K 연료
# arr: 손님의 출발지와 목적지를 담을 리스트
arr = [[[] for _ in range(N)] for _ in range(N)]
# board: 길이 갈 수 있는지 없는지 알려줄 리스트
board = [[*map(int,input().split())] for _ in range(N)]

# 현위치
a,b = map(lambda x:int(x)-1,input().split())

# 손님은 최대 400명
for i in range(1,M+1):
    x1,y1,x2,y2 = map(lambda x:int(x)-1,input().split())
    arr[x1][y1].append(i)
    arr[x2][y2].append(1000+i)        # 도착지를 1000+i로 해싱

# 시작
while K and M:
    a,b,x,spend = find_start(a,b)
    K -= spend
    if K < 0:
        exit(print(-1))

    a,b,spend = find_end(a,b,x+1000)
    K -= spend
    if K < 0:
        exit(print(-1))
    
    K += spend*2
    M -= 1

print(-1 if M else K)