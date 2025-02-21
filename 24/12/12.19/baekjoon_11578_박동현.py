'''
팀원 모집

백트래킹, 비트마스킹

연습문제
'''
def backtrack(idx=0,res=0,c=0):
    global cnt
    if (1<<N)-1 == res:
        cnt = min(cnt, c)
        return
    
    if idx == M:
        return
    
    backtrack(idx+1, res|data[idx], c+1)
    backtrack(idx+1, res, c)


N,M = map(int,input().split())

data = []
for _ in range(M):
    a, *d = map(int,input().split())
    tmp = 0
    for i in d:
        tmp |= 1<<i-1
    
    data.append(tmp)
cnt = float('inf')
backtrack()
print(cnt if cnt != float('inf') else -1)