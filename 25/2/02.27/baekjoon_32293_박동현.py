import sys; input = lambda: sys.stdin.readline().strip()


for _ in range(int(input())):
    N = int(input())
    S = input()
    stack = []
    for char in S:
        stack.append(char)
        if len(stack) < 2: continue

        cnt = 0
        while stack[-3:] == ["A", "B", "B"]:
            cnt += 1
            for _ in range(3):
                stack.pop()
            stack.append("B")
        
        for _ in range(cnt):
            stack.append("A")

    print("".join(stack))