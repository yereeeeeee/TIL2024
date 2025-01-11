'''
압축

스택

문제에 주어진 괄호의 특성에 따라 조건을 정함
'''
ans, stack = 0, []
for char in input():
    if char == "(":
        stack.append((int(last), ans-1))
        ans = 0
    elif char  == ")":
        k, prev_ans = stack.pop()
        ans = k*ans + prev_ans
    else:
        ans += 1
        last = char
print(ans)