import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    x, y = map(int, input().split())

    distance = y - x    # x와 y 사이 거리
    move_dist = 0       # 이동 거리
    cnt = 0             # 공간 장치 이동 횟수
    moving_cnt = 0      # 반복 횟수

    while move_dist < distance:
        cnt += 1
        # 공간 장치 이동 횟수는 (공간 장치 이동 횟수 % 2)
        if cnt % 2:
            # 만약 공간 장치 이동 횟수가 홀수라면 반복 횟수 증가
            moving_cnt += 1

        move_dist += moving_cnt

    print(cnt)