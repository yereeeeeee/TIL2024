def check_balance():
    res = 0
    for i in range(N-1, 0, -1):
        res += boxes[i]
        center = res / (N-i)
        if center <= boxes[i-1] - K or center >= boxes[i-1] + K:
            return False
    return True

N,K = map(int,input().split())
boxes = [*map(int,input().split())]

print("stable" if check_balance() else "unstable")