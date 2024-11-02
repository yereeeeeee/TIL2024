import sys; input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def post_order(start,end):
    if start>end: return
   
    mid = end + 1 
    for i in range(start+1,end+1):
        if arr[start]<arr[i]:
            mid = i
            break
    
    post_order(start+1, mid-1) 
    post_order(mid, end)
    print(arr[start])


arr = []
while True:
    try: arr.append(int(input()))
    except: break

start = 0
end = len(arr)-1

post_order(start,end)