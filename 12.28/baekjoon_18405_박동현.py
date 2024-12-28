'''
경쟁적 전염

BFS?

딕셔너리에 위치를 기록하며 순회
'''
import sys; input = sys.stdin.readline


def spread():
    for _ in range(S):

        for i, items in sorted(virus.items()):
            tmp = []
            for item in items:
                x,y = item
                
                for dx,dy in dr:
                    di,dj = x+dx, y+dy
                    if 0<=di<N and 0<=dj<N:
                        if not arr[di][dj]:
                            arr[di][dj] = i
                            tmp.append((di,dj))
            if arr[X-1][Y-1]: 
                return arr[X-1][Y-1]
            virus[i].extend(tmp)
    return arr[X-1][Y-1]


dr = (1,0),(0,1),(-1,0),(0,-1)

N,K = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

S,X,Y = map(int,input().split())
virus = dict()
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            virus.setdefault(arr[i][j], []).append((i,j))

print(spread())