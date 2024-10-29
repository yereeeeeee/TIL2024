import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 각 CCTV의 종류별 방향 설정
dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# 사각지대 카운팅 함수
def cnt():
    tmp = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                tmp += 1
    return tmp

# CCTV 감시 영역 표시 함수
def watch(x, y, dirs):
    changed = []
    for d in dirs:
        nx, ny = x + dx[d], y + dy[d]
        while 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 6:  # 벽을 만나면 감시 종료
                break
            if arr[nx][ny] == 0:  # 빈 공간이라면 감시 가능
                arr[nx][ny] = '#'
                changed.append((nx, ny))
            nx += dx[d]
            ny += dy[d]
    return changed

# 재귀적으로 모든 CCTV 감시 영역 처리
def sol(cctv_cnt):
    global answer

    if cctv_cnt == len(cctv_pos):
        answer = min(answer, cnt())
        return

    x, y, cctv_type = cctv_pos[cctv_cnt]
    for dirs in dir[cctv_type]:
        changed = watch(x, y, dirs)
        sol(cctv_cnt + 1)
        for nx, ny in changed:
            arr[nx][ny] = 0  # 감시 구역 원상 복구

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cctv_pos = []
answer = 100

# CCTV 위치 기록
for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            cctv_pos.append((i, j, arr[i][j]))

sol(0)
print(answer)
