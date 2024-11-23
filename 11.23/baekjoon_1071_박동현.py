'''
소트

그리디

개수가 최대 50개이기 때문에, remove를 써도 시간은 널널하다.
딕셔너리에 넣고, 키값을 정렬해 관리하면서, 딕셔너리 값이 0이 되면 값을 제거하는 방식
'''
N = int(input())
arr = [*map(int,input().split())]

data = dict()
for i in arr:
    data[i] = data.get(i,0)+1

ans = []
keys = sorted(data.keys())

while len(ans) != N:
    if len(keys) == 2 and keys[1]-keys[0] == 1:
        ans.append(keys[1])
        data[keys[1]] -= 1
        if data[keys[1]] == 0:
            data.pop(keys[1])
            keys.remove(keys[1])
    else:
        for key in keys:
            if ans and ans[-1] + 1 == key:
                continue

            ans.append(key)
            data[key] -= 1
            if data[key] == 0:
                keys.remove(key)
                data.pop(key)
            break
print(*ans)