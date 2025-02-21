'''
매직스타

백트래킹, 구현

0 2 5 7
1 2 3 4
7 8 9 10
4 6 9 11
모두 같은 값이 되기 위해서는, 각 줄이 26이 되어야 한다.
'''
def is_valid(idx, value, data):
    tmp = [arr[i] for i in data]
    tmp[data.index(idx)] = value
    if all(tmp):
        return sum(tmp) == 26
    return sum(tmp) < 26

def to_alphabet(num):
    return chr(num-1+ord("A"))

def backtrack(visit, idx=0):
    if all(arr):
        ans = [to_alphabet(x) for x in arr]

        answer = [['.']*9 for _ in range(5)]
        positions = (0,4),(1,1),(1,3),(1,5),(1,7),(2,2),(2,6),(3,1),(3,3),(3,5),(3,7),(4,4)
        for i in range(12):
            x,y = positions[i]
            answer[x][y] = ans[i]
        
        for a in answer:
            print(*a, sep="")
        exit()
    
    if arr[idx]:
        backtrack(visit, idx+1)
        return
    
    for i in range(1,13):
        if visit&1<<i: continue
        for data in lines[idx]:
            if not is_valid(idx, i, data): break
        else: 
            arr[idx] = i
            backtrack(visit|1<<i, idx+1)
            arr[idx] = 0


lines = dict()
for i in range(12):
    for data in [[0,2,5,7], [1,2,3,4], [7,8,9,10], [4,6,9,11], [1,5,8,11], [0,3,6,10]]:
        if i in data:
            lines.setdefault(i, list()).append(data)

arr = []
for _ in range(5):
    tmp = list(input())
    for a in tmp:
        if a != ".":
            if a == "x":
                arr.append(0)
            else:
                arr.append(ord(a)-ord("A")+1)

visit = 0
for i in range(12):
    if arr[i]: visit |= 1<<arr[i]

backtrack(visit)