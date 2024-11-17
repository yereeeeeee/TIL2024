'''
선분 교차

17386과 17387 두 문제가 사실상 거의 똑같은데, 왜 동일한 코드로 풀리지 않는가?
사실 잘 모르겠음. 17386에 해당하는 반례는 찾았는데 왜 무리 없이 통과하는지도 잘 모르겠음
'''

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (x3-x1) *(y2-y1)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ans = 0
check = False

a = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
b = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

if a==0 and b==0:  
    check = True
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):  
        ans = 1
if a<=0 and b<=0:
    if not check:
        ans = 1

print(ans)