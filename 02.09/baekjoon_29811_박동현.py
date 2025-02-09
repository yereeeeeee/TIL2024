import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def make_enumerated_heap(lst,idx=1):
    res = []
    for k in lst:
        heappush(res, (k,idx))
        idx += 1
    return res

def U(x,y):
    x,y = map(int,(x,y))
    if x <= N:
        heappush(arr_hq, (y, x))
        arr[x-1]=y
    else:
        heappush(brr_hq, (y, x))
        brr[x-N-1]=y

def L(*args):
    while arr_hq[0][0] != arr[arr_hq[0][1]-1]:
        heappop(arr_hq)
    
    while brr_hq[0][0] != brr[brr_hq[0][1]-1-N]:
        heappop(brr_hq)
    print(arr_hq[0][1], brr_hq[0][1])

cmd = {
    "U": U,
    "L": L
}

N,M = map(int,input().split())
arr = [*map(int,input().split())]
brr = [*map(int,input().split())]

arr_hq = make_enumerated_heap(arr)
brr_hq = make_enumerated_heap(brr, N+1)

for _ in range(int(input())):
    c, *args = input().split()
    cmd[c](*args)