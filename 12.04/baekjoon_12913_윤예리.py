import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

INF = float('inf')
distance = [[INF] * n for _ in range(k + 1)]

def dijkstra():
    q = []
    heappush(q, (0, 0, 0))  # (현재 비용, 현재 노드, 사용한 포션 수)
    distance[0][0] = 0

    while q:
        cur_cost, cur_node, cur_k = heappop(q)

        if cur_cost > distance[cur_k][cur_node]:
            continue

        for next_node in range(n):
            if cur_node == next_node:
                continue

            next_cost = arr[cur_node][next_node]

            # 포션 사용하지 않는 경우
            if distance[cur_k][next_node] > cur_cost + next_cost:
                distance[cur_k][next_node] = cur_cost + next_cost
                heappush(q, (distance[cur_k][next_node], next_node, cur_k))

            # 포션 사용하는 경우
            if cur_k < k and distance[cur_k + 1][next_node] > cur_cost + (next_cost / 2):
                distance[cur_k + 1][next_node] = cur_cost + (next_cost / 2)
                heappush(q, (distance[cur_k + 1][next_node], next_node, cur_k + 1))

dijkstra()
answer = min(distance[i][1] for i in range(k + 1))
print(answer)
