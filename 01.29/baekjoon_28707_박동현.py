'''
배열 정렬

해시맵, 다익스트라

다익스트라를 하는데, 노드는 정렬 중인 튜플이다.
'''
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def swap(a,b, tp: tuple):
    res = list(tp)
    res[a],res[b] = res[b],res[a]
    return tuple(res)

N = int(input())
arr = [0]+[*map(int,input().split())]
query = [[*map(int,input().split())] for _ in range(int(input()))]

start = tuple(arr)
end = tuple(sorted(arr))

distance = dict()
hq = [(0, start)]
distance[start] = 0
while hq:
    dist_now, now = heappop(hq)

    for a,b,cost in query:
        nxt = swap(a,b, now)
        dist_nxt = dist_now + cost
        if distance.get(nxt, float('inf')) > dist_nxt:
            distance[nxt] = dist_nxt
            heappush(hq, (dist_nxt, nxt))

print(distance.get(end, -1))