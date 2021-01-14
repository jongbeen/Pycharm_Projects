def solution(triangle):
    N = len(triangle)
    dp = triangle
    if N == 1:
        return dp[0][0]
    dp[0] = triangle[0]
    dp[1] = [triangle[1][0]+triangle[0][0], triangle[1][1]+triangle[0][0] ]

    if N == 2:
        return max(dp[1])

    for i in range(2,N):
        for j in range(i+1):
            if j==0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j==i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]

    answer = max(dp[N-1])
    for i in dp:
        print(i)
    return answer

t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(t))