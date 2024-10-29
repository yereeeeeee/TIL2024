n = int(input())
arr = [0] * (n+1)

def check(x):
    # 대각선에 있으면 True 없으면 False
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == abs(x-i):
            return False

    return True

answer = 0
def sol(x):
    global answer

    if x == n:
        answer += 1
        return

    for i in range(n):
        arr[x] = i
        if check(x):
            sol(x+1)

sol(0)
print(answer)