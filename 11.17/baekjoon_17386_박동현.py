# 두 점을 기반으로 일차 방정식을 만들고, 이를 기반으로 연립방정식을 풀이한다.
# 연립 방정식의 해가 없는 경우 => 평행선
# 연립 방정식의 해가 무한히 많은 경우 => 겹치는 선
# 연립 방정식의 해가 하나인 경우 => 교차
# 단, 방정식의 해가 두 점 사이에 있어야한다. (마지막에 검증)
def make_eqaution(x1,y1, x2,y2):
    # y = ax + b 형태로 나타낸다면, a,b 를 반환
    # 기울기 계산
    ## x = 2 형태의 그래프가 나오는 경우
    if x1==x2:
        return 
    ## y = 2 형태의 그래프가 나오는 경우
    if y1==y2:
        return 0, y1
    ## 그 외 
    a = (y2-y1) / (x2-x1)
    # 기울기를 통해 x = 0 일 때 y의 값 계산
    b = y1-x1*a 
    return a, b


def is_cross(x1,x2,x3,x4,y1,y2,y3,y4):
    if x1 > x2: x1,x2 = x2,x1
    if x3 > x4: x3,x4 = x4,x3
    if y1 > y2: y1,y2 = y2,y1
    if y3 > y4: y3,y4 = y4,y3

    if x1 <= x <= x2 and x3 <= x <= x4:
        if y1 <= y <= y2 and y3 <= y <= y4:
            return 1
    return 0


x1,y1, x2,y2 = map(int,input().split())
x3,y3, x4,y4 = map(int,input().split())

# 기울기: y의 증가량 / x의 증가량
x=0
check = True
if x1!=x2:
    check = True
    a,b = make_eqaution(x1,y1,x2,y2)
else:
    x = x1

if x3!= x4:
    check = False
    c,d = make_eqaution(x3,y3,x4,y4)
else :
    if x1==x2:
        if x1==x3:
            exit(print(1))z
        else:
            exit(print(0))
    else:
        x=x3
    
# y = ax + b
# y = cx + d
# (a-c)x = d-b
if not x:
    if a==c:
        if d==b:
            exit(print(1))
        else:
            exit(print(0))
    
    else:
        x = (d-b) / (a-c)
if check:
    y = a*x + b
else:
    y = c*x + d


print(is_cross(x1,x2,x3,x4,y1,y2,y3,y4))