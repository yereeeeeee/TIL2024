import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]

# 머리
def head():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "*":
                return i, j

i, j = head()
print(i+2, j+1)

# 왼쪽 팔
def left_arm(i, j):
    cnt = 0
    j -= 1
    while True:
        if j < 0 or arr[i][j] == "_":
            return cnt

        j -= 1
        cnt += 1

# 오른쪽 팔
def right_arm(i ,j):
    cnt = 0
    j += 1
    while True:
        if j >= n or arr[i][j] == "_":
            return cnt

        j += 1
        cnt += 1

# 허리
x, y = 0, 0
def back(i, j):
    global x, y
    cnt = 0
    i += 1
    while True:
        if i >= n or arr[i][j] == "_":
            x = i-1
            y = j
            return cnt

        i += 1
        cnt += 1

print(left_arm(i+1, j), end=" ")
print(right_arm(i+1, j), end=" ")
print(back(i+1, j), end=" ")

# 왼쪽 다리
def left_leg(x, y):
    cnt = 0
    x += 1
    y -= 1
    while True:
        if x >= n or arr[x][y] == "_":
            return cnt

        x += 1
        cnt += 1

# 오른쪽 다리
def right_leg(x, y):
    cnt = 0
    x += 1
    y += 1
    while True:
        if x >= n or arr[x][y] == "_":
            return cnt

        x += 1
        cnt += 1

print(left_leg(x, y), end=" ")
print(right_leg(x, y), end=" ")