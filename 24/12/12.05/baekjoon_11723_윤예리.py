import sys
input = sys.stdin.readline

m = int(input())
s = 0  # 비트마스킹용 변수

for _ in range(m):
    arr = input().split()
    cmd = arr[0]

    if cmd == 'add':
        s |= (1 << (int(arr[1]) - 1))

    elif cmd == 'remove':
        s &= ~(1 << (int(arr[1]) - 1))

    elif cmd == 'check':
        if s & (1 << (int(arr[1]) - 1)):
            print(1)
        else:
            print(0)

    elif cmd == 'toggle':
        s ^= (1 << (int(arr[1]) - 1))

    elif cmd == 'all':
        s = (1 << 20) - 1  # 1부터 20까지 모든 비트를 1로 설정

    elif cmd == 'empty':
        s = 0  # 모든 비트를 0으로 설정

# import sys
# input = sys.stdin.readline
#
# m = int(input())
# s = []
#
# for _ in range(m):
#     arr = input().strip().split()
#
#     if arr[0] == 'add' and arr[1] not in s:
#         s.append(arr[1])
#
#     elif arr[0] == 'remove' and arr[1] in s:
#         s.remove(arr[1])
#
#     elif arr[0] == 'check':
#         if arr[1] in s:
#             print(1)
#         else:
#             print(0)
#
#     elif arr[0] == 'toggle':
#         if arr[1] in s:
#             s.remove(arr[1])
#         else:
#             s.append(arr[1])
#
#     elif arr[0] == 'all':
#         s = [i for i in range(1, 21)]
#
#     elif arr[0] == 'empty':
#         s = []