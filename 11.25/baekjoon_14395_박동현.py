'''
4연산

문자열,BFS

생각보다 조건이 깔끔하지 않음
'''


from collections import deque


N,M = map(int,input().split())
q = deque([("",N)])

visit = set()

if M == 0: exit(print("/"))
if N == M: exit(print(0))

while q:
    ans, now = q.popleft()
    
    if now == M: exit(print(ans))

    if now < M:
        if now > 1 and now*now not in visit: 
            visit.add(now*now)
            q.append((ans+"*", now*now))

        if now+now not in visit:
            visit.add(now+now)
            q.append((ans+"+", now+now))

    if now and 1 not in visit:
        visit.add(1)
        q.append((ans+"/", 1))

print(-1)