'''
Boggle

트라이, 백트래킹, 비트마스킹

트라이를 구성하고, 백트래킹을 통해 퍼즐 내에 있는 단어를 찾아내는 내용이다.
백트래킹 시작점을 잘못 잡아서 10번 넘게 틀렸다.

백트래킹 방문 표시를 visit 배열로 하려다가, 
비트마스킹으로 해도 부담이 없을 것 같아 연습삼아 비트마스킹도 추가했다.


'''


import sys; input = lambda: sys.stdin.readline().strip()


dr = (1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)
score_count = [0,0,0,1,1,2,3,5,11]

def insert(text):
    now = trie
    for char in text:
        now[char] = now.setdefault(char, dict())
        now = now[char]
    # 단어의 마지막엔 0을 두어 끝을 표시한다.
    now[0] = text

def backtrack(i,j,now,visit):
    # 단어가 있는 경우 answer에 추가한다. (이 때, 끝내면 안된다.)
    if 0 in now:
        answer.add(now[0])

    # BFS방식으로 순회 
    for di,dj in dr:
        x,y = i+di, j+dj
        
        if 0<=x<4 and 0<=y<4:
            if visit & 1 << x*4+y: continue

            if arr[x][y] in now:
                backtrack(x,y, now[arr[x][y]], visit | 1<<x*4 +y)
        

# trie를 딕셔너리 방식으로 구현해 넣는다.
trie = dict()
for word in [input() for _ in range(int(input()))]: 
    insert(word)
    
input()     # 빈줄 처리용

for _ in range(int(input())):
    # Boggle 배열
    arr = [list(input()) for _ in range(4)]

    answer = set()
    # 배열을 순회하면서 
    for i in range(4):
        for j in range(4):
            # 트라이에 해당 철자가 있다면
            if arr[i][j] in trie:
                # 방문 표시를 하고 출발
                # backtrack(i,j, trie, 0) : 이렇게 해서 틀림
                backtrack(i,j, trie[arr[i][j]], 1 << i*4 + j)

    # answer에 찾은 단어들을 모으고, 최종적으로 점수를 계산한다.
    score = 0
    cnt = len(answer)
    max_text = ""

    for ans in answer:
        score += score_count[len(ans)]
        
        if len(ans) > len(max_text):
            max_text = ans

        elif len(ans) == len(max_text):
            max_text = min(ans, max_text)
    # 출력
    print(score, max_text, cnt)

    input()     # 빈줄 처리용