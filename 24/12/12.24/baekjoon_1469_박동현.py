'''
숌 사이 수열

백트래킹

문제가 요구하는 대로 ans 배열에 숫자를 위치시키고, 
끝까지 진행된 경우 answer배열에 옮겨 정렬 후 가장 앞의 배열을 출력
'''
def backtrack(ans, idx=0):
    if idx == N:
        return answer.append(ans[:])
    
    for i in range(2*N):
        now = arr[idx]

        if now + i + 1 >= 2*N: continue
        if ans[i] != -1: continue
        if ans[i+1+now] != -1: continue

        ans[i] = now
        ans[i+1+now] = now
        
        backtrack(ans, idx+1)
        
        ans[i] = -1
        ans[i+1+now] = -1


N = int(input())
arr = [*map(int,input().split())]

ans = [-1]*N*2
answer = []
backtrack(ans)

if answer:
    print(*sorted(answer)[0])
else:
    print(-1)