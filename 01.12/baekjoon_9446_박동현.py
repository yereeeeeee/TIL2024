'''
텀 프로젝트

DFS

사이클을 이루고 있는지 어떻게 확인할 것인가? 에 관한 문제
사이클을 확인하는 방법에 대해서 더 고민해봐야겠다.
바로 떠오르는 풀이가 시간초과, 메모리초과 연달아 뜨는걸 보니 기초부터 잘못됐다는 생각이 들었다.
'''
import sys; input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())

    arr = [*map(lambda x: int(x)-1, input().split())]
    
    child = [0]*N
    
    for i in arr:
        child[i] += 1
    leaves = [i for i in range(N) if child[i] == 0]

    for leaf in leaves:
        idx = arr[leaf]

        child[idx] -= 1
        
        if child[idx] == 0:
            leaves.append(idx)
    print(len(leaves))