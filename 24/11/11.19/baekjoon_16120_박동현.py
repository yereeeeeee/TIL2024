stack = []
for char in input():
    stack.append(char)
    if len(stack) >= 4 and "".join(stack[-4:]) == "PPAP":
        for _ in range(3): stack.pop()
print("PPAP" if stack[0] == "P" else "NP")