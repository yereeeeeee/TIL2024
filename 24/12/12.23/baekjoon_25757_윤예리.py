import sys
input = sys.stdin.readline

game = {
    "Y": 1,
    "F": 2,
    "O": 3
}
n, g = input().split()
n = int(n)
k = game[g]

players = set(input() for _ in range(n))
m = len(players)
print(m//k)