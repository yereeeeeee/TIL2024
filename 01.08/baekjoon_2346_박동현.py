'''
풍선 터뜨리기

덱

예전에 제대로 이해 못해서 푸는 김에 겸사겸사 숏코딩 (131B)
'''
from collections import*
input()
q=deque(enumerate(map(int,input().split())))
while q:i,v=q.popleft();print(i+1);q.rotate(-v+(v>0))