def backtrack(value=""):
    for i in range(10):
        if not value or int(value[-1]) > i:
            if len(value) < 10: # 최대가 9876543210
                res.append(int(value+str(i)))
                backtrack(value+str(i))

res = []
num = int(input()) - 1
backtrack()
print(-1 if num >= len(res) else sorted(res)[num])
