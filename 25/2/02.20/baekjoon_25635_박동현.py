N = int(input())
arr = [*map(int,input().split())]

total_arr = sum(arr)
max_arr = max(arr)

valid = (total_arr+1) // 2

if valid < max_arr:
    print((total_arr - max_arr) * 2 + 1)
else:
    print(total_arr)