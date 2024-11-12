import sys
input = sys.stdin.readline
from collections import deque

dn = [-1, 0, 1, 0]
dm = [0, 1, 0, -1]

n, m, k = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]
q = deque([(0, 0, 0, 1)])   # k, n, m, 현재까지의 거리
visited[0][0][0] = 1

while q:
    ck, cn, cm, dist = q.popleft()
    if cn == n-1 and cm == m-1:
        print(dist)
        break

    day = dist % 2
    for d in range(4):
        nn, nm = cn + dn[d], cm + dm[d]
        if 0 <= nn < n and 0 <= nm < m:
            if visited[ck][nn][nm] == 0 and graph[nn][nm] == 0:
                visited[ck][nn][nm] = dist
                q.append((ck, nn, nm, dist + 1))

            elif ck < k and graph[nn][nm] == 1 and visited[ck+1][nn][nm] == 0:
                if day:
                    visited[ck+1][nn][nm] = dist
                    q.append((ck+1, nn, nm, dist+1))
                else:
                    q.append((ck, cn, cm, dist+1))

else:
    print(-1)