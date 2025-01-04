'''
친구 네트워크

유니온 파인드, 해시맵

유니온 파인드를 통해 동적으로 집합을 관리

*발생한 문제:
ans 라는 문자열에 해당 문제의 답안을 모두 저장한 후, 마지막에 출력하는 방식을 선택한 경우 7748ms 가 걸렸다.
문제에서 요구한 방식으로 한 줄의 입력마다 출력을 처리한 경우 252ms가 걸렸는데, 이는 30배 가량 차이가 나게된다.
I/O 에 관해서 조금 더 생각해봐야겠다.
'''
import sys; input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x,y):
    x,y = find(x), find(y)

    if x == y: return
    parent[y] = x
    visit[x] += visit[y]

    
for _ in range(int(input())):
    parent = dict()
    visit = dict()

    for _ in range(int(input())):
        a,b = input().split()

        if a not in parent:
            parent[a] = a
            visit[a] = 1
        
        if b not in parent:
            parent[b] = b
            visit[b] = 1
        
        union(a,b)

        print(visit[find(a)])

'''
풀이 2

직관적으로 떠오른 풀이.
동적으로 관리하는 부분을 떼어내 수동적으로 관리할 수도 있다.
유니온 파인드보다 시간과 공간 복잡도가 조금 더 발생하기는 하지만, 이 또한 적절한 시간 내에서 풀이가 가능하다.
'''
import sys; input = sys.stdin.readline


for _ in range(int(input())):

    data = dict()
    group = dict()
    cnt = 0
    for _ in range(int(input())):
        a,b = input().split()
        if a not in data and b not in data:
            data[a] = cnt
            data[b] = cnt
            group[cnt] = {a,b}
            cnt += 1
        else:
            if a in data and b in data:
                if data[a] != data[b]:
                    tmp = group.pop(data[b])

                    for i in tmp:
                        data[i] = data[a]

                    group[data[a]] |= tmp

            elif a in data:
                data[b] = data[a]
                group[data[a]].add(b)

            elif b in data:
                data[a] = data[b]
                group[data[b]].add(a)
                
        print(len(group[data[a]]))