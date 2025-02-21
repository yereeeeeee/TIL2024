'''
볼록 껍질

CCW(벡터 외적) 문제에서 발전해서,
각각의 점들의 관계를 확인하고, 개수를 출력
'''

def cp(x1,x2,x3):
    # 외적 Cross Product 공식을 이용
    # 0이면 일직선, 양수면 시계방향, 음수면 반시계 방향으로 이어져 있음을 나타낸다.
    # 한 방향만 선택하면 되기 때문에, 일단 0 이상으로 정했다.
    return ((x1[0] * x2[1]) + 
            (x2[0] * x3[1]) + 
            (x3[0] * x1[1]) - 
            (x1[1] * x2[0]) - 
            (x2[1] * x3[0]) - 
            (x3[1] * x1[0])) >=0


def convex_hull(points):
    # 왼 -> 오 
    cw = []
    for point in points:
        while len(cw) > 1 and cp(cw[-2], cw[-1], point):
            cw.pop()
        cw.append(point)

    # 오 -> 왼
    ccw = []
    for point in points[::-1]:
        while len(ccw) > 1 and cp(ccw[-2], ccw[-1], point):
            ccw.pop()
        ccw.append(point)

    # 두가지 방향을 더하고, 시작점은 빼서 결과를 구성
    # 중간을 기준으로, 왼쪽을 시계방향으로 돌렸으면, 오른쪽은 반시계방향으로 돌려야하고, 이 두개를 더하는게 맞다
    # 그리고, 두 점들이 합쳐지면서 2개의 점이 겹칠 수 있기 때문에 하나씩 빼주면 된다.
    return len(cw[:-1]) + len(ccw[:-1])


N = int(input())
arr = sorted([[*map(int,input().split())] for _ in range(N)])

print(convex_hull(arr))