import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    # 팀별 데이터 관리: 선수 수, 점수 리스트, 점수 합계
    manage = {}
    for i in range(n):
        if arr[i] not in manage:
            manage[arr[i]] = [1, [], 0]  # 선수 수, 점수 리스트, 점수 합계
        else:
            manage[arr[i]][0] += 1

    # 제외 팀: 6명 미만인 팀
    contain = set(k for k, v in manage.items() if v[0] < 6)

    grade = 1
    for i in range(n):
        if arr[i] in contain:
            continue
        manage[arr[i]][1].append(grade)  # 등수 추가
        if len(manage[arr[i]][1]) <= 4:  # 상위 4명만 점수 합산
            manage[arr[i]][2] += grade
        grade += 1

    # 유효한 팀만 모아 정렬 기준 적용
    answer = []
    for k, v in manage.items():
        if len(v[1]) >= 5:  # 6명의 점수를 가진 팀만 고려
            answer.append([k, v[1][4], v[2]])  # 팀 번호, 5번째 점수, 점수 합계

    # 정렬: 1순위 점수 합계, 2순위 5번째 점수
    answer.sort(key=lambda x: (x[2], x[1]))

    # 우승 팀 출력
    print(answer[0][0])
