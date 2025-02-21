'''
별 찍기 - 10

재귀

재미있는 별찍기. 
가운데를 비워야하니 가중치가 (next_size, next_size)인 경우를 제외하고 재귀를 수행하면 가운데가 비게 된다.
'''
def make_pattern(size, i=0, j=0):
    if next_size:=size//3:
        weights = (0, next_size, next_size*2)
        for wi in weights:
            for wj in weights:
                # 가운데 비우기
                if wi==wj==next_size: continue
                make_pattern(next_size, i+wi, j+wj)
    answer[i][j] = "*"

N = int(input())
answer = [[" "]*N for _ in range(N)]
make_pattern(N)
for ans in answer:
    print(*ans, sep="")
