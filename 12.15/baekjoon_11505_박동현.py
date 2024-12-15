'''
구간 곱 구하기

세그먼트 트리

일반적인 세그먼트 트리에서 값을 리스트로 저장하면서
0이 입력되면 0의 개수를, 다른 자연수가 입력되면 일반적인 곱연산을 수행하고
출력 시 입력된 0의 값을 참조해 0이 하나라도 입력되어 있다면 0을 출력하고
그렇지 않다면 앞에 저장된 곱연산값을 출력한다.
'''
import sys; input=sys.stdin.readline


def init(start, end, idx=1):
    if start == end:
        if arr[start-1] == 0:
            tree[idx][1] += 1
        else:
            tree[idx][0] = arr[start-1]
    else:
        mid = (start+end) // 2
        
        a = init(start, mid, idx*2)
        b = init(mid+1, end, idx*2+1)
        tree[idx][0] = a[0] * b[0] % div
        tree[idx][1] = a[1] + b[1]

    return tree[idx]

# 1: x인덱스의 값을 y로 바꾼다.
def update_query(x,y):
    res = update(0, N-1, arr[x], y, 1, x)
    arr[x] = y

# 2: x부터 y인덱스까지의 곱을 구한다
def find_query(x,y):
    res = find(0, N-1, x, y, 1)
    print(0 if res[1] else res[0]%div)

def update(start, end, old_data, new_data, idx, new_idx):
    if start > new_idx or end<new_idx: return
    
    if start == end:
        if old_data == 0:
            tree[idx][1] -= 1
        else:
            tree[idx][0] //= old_data
        if new_data == 0:
            tree[idx][1] += 1
        else:
            tree[idx][0] *= new_data
            tree[idx][0] %= div
        return

    mid = (start+end) // 2
    update(start, mid, old_data, new_data, idx*2, new_idx)
    update(mid+1, end, old_data, new_data, idx*2+1, new_idx)

    tree[idx][0] = tree[idx*2][0] * tree[idx*2+1][0] % div
    tree[idx][1] = tree[idx*2][1] + tree[idx*2+1][1]


def find(start, end, left, right, idx):
    if start > right or end < left: 
        return [1,0]
    if start >= left and end <= right:
        return tree[idx]
    
    mid = (start+end)//2

    a = find(start, mid, left, right, idx*2)
    b = find(mid+1, end, left, right, idx*2+1)
    return [a[0]*b[0]%div, a[1]+b[1]]

# 쿼리 처리 및 나머지 연산
query = {
    1: lambda x,y: update_query(x-1,y),
    2: lambda x,y: find_query(x-1,y-1)
}
div = 1000000007

# 입력
N,M,K = map(int,input().split())
arr = [int(input()) for _ in range(N)]
tree = [[1,0] for _ in range(4*N)]

init(1,N)
for _ in range(M+K):
    a,b,c = map(int,input().split())
    query[a](b,c)