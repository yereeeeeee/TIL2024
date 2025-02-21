'''
오민식의 고민

벨만-포드

벨만-포드 알고리즘은 음의 가중치를 가진 그래프 내부에서의 최단거리와 사이클을 찾아내는 알고리즘이다.

현실에서는 음의 가중치가 존재하는 경우가 거의 없기에, 현실적이지 않다는 말을 듣긴 했다.

원래 알고 있던 벨만-포드 알고리즘이 심각한 수준으로 느린코드였음

다시 내용 숙지하고, 변형 벨만-포드 알고리즘 문제를 풀어봄

1. 도착지에 갈 수 있는 그래프인지,
2. 사이클이 있다면, 해당 사이클이 도착지에 갈 수 있는 사이클인지

확인해 최종 답안을 출력한다.
'''


import sys; input = sys.stdin.readline


def bellman_ford():
    distance = [-float('inf')]*N
    distance[S] = benefit[S]

    for i in range(N-1):
        for s,e,w in graph:
            if distance[s] != -float('inf') and distance[s] + w > distance[e]:
                distance[e] = distance[s] + w
                
    if distance[E] == -float('inf'):
        return "gg"
    
    for s,e,w in graph:
        if distance[s] != -float('inf') and distance[s] + w > distance[e]:
            if dfs(e):
                return "Gee"

    return distance[E]

def dfs(start):
    stack = [start]
    visit = [False]*N
    while stack:
        now = stack.pop()
        if now == E:
            return True
        
        if not visit[now]:
            visit[now] = True
            for s,e,c in graph:
                if s != now: continue
                stack.append(e)
    return False

N,S,E,M = map(int,input().split())

tmp = [[*map(int,input().split())] for _ in range(M)]
benefit = [*map(int,input().split())]
graph = [] 
for s,e,c in tmp:
    graph.append((s,e,benefit[e] - c))
print(bellman_ford())