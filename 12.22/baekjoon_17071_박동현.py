'''
숨바꼭질 5

BFS

BFS가 어려운게 아니라 이미 통과한 지점을 어떻게 처리할지를 생각하는게 어려움
짝수번째에 도착했다면 모든 짝수번째에서 멈출 수 있다. 를 생각할 수 있어야 하는 문제
'''


from collections import deque


def in_range(num):
    return 0 <= num <= 500000

def dfs(N,K):
    if N == K: return 0

    visit=[[-1,-1] for _ in range(500001)]
    
    q = deque([N])

    time = 1
    K += time

    while True:
        if not in_range(K): break

        next_q = deque()

        while q:
            now = q.popleft()

            for nxt in [now-1, now+1, now*2]:
                
                if in_range(nxt) and visit[nxt][time%2] == -1:
                    visit[nxt][time%2] = time
                    next_q.append(nxt)

        if visit[K][time%2] != -1: return time

        time += 1
        K += time

        q = next_q

    return -1

print(dfs(*map(int,input().split())))