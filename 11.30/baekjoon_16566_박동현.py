'''
카드 게임

이분 탐색

이분 탐색을 하면서, 방문한 위치에 대해서는 값을 더 올려 방문하는 방식
근데 왜 python으로는 시간초과 나고 pypy로만 가능하지?
'''

N,M,K = map(int,input().split()) 
# 뽑은 카드, M: 카드 개수 ( 1 이상 N 이하 )
cards = sorted([*map(int,input().split())])

visit = [False] * (M)
# 철수가 i번째로 내는 카드의 번호 
for i in map(int,input().split()):
    left, right = 0, M-1

    while left <= right:
        mid = (left+right) // 2
        if i < cards[mid]:
            right = mid - 1
        else:
            left = mid + 1

    while visit[left]:
        left += 1
    visit[left] = True
    
    print(cards[left])