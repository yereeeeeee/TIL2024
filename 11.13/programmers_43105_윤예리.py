def solution(triangle):
    # 위에서 아래로 내려가면서 더해주기
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            # 먼저 온 애들이랑 비교해주면서 큰 값 갱신해줄거임
            # 아래로 가기
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])        
            # 오른쪽 아래로 가기
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

    # 마지막 줄의 최대값 print
    return max(dp[-1])