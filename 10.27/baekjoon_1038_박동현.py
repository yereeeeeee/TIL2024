def backtrack(idx, res=""):
    if idx == 0:
        return ans.append(res)

    for i in range(10):
        if not res or res[-1] > str(i):
            backtrack(idx-1, res+str(i))

N = int(input())
ans = []
for i in range(1,11):
    backtrack(i)
print(ans[N] if N < len(ans) else -1)

'''
문제: 9876543210 처럼 감소하는 수를 찾는 문제
그 중 N번 째 수를 찾아 출력

풀이: 
백트래킹을 통해 모든 감소하는 수를 찾아 ans 배열에 저장하고, 해당 인덱스의 값을 출력
최대 9876543210 이기 때문에, 1자리수부터 10자리수까지 백트래킹을 진행하면 된다.
'''