'''
휴대폰 자판

트라이

트라이로 저장을 하고, 
문제에서 요구하는 조건에 맞게 search함수를 만들어 출력한다.
'''
import sys; input = sys.stdin.readline


def insert(word):
    now = trie
    for char in word:
        now = now.setdefault(char, dict())
    now[0] = True

def search(now, cnt=0):
    global ans
    
    for char in now:
        if char == 0:
            ans += cnt
            continue

        if len(now)==1:
           search(now[char], cnt)
           continue

        search(now[char], cnt+1)    

while True:
    try:
        N = int(input())
        words = [input().strip() for _ in range(N)]
        
        trie = dict()
        for word in words:
            insert(word)

        ans = 0
        search(trie)

        if len(trie) == 1:
            ans += N
        
        print(f"{ans/N:.2f}")

    except:
        break
