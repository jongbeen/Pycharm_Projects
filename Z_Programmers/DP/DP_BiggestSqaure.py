def solution(board):
    n = len(board)
    m = len(board[0])
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = board[i][0]
    for i in range(m):
        dp[0][i] = board[0][i]

    for i in range(1,n):
        for j in range(1,m):
            if board[i][j]==1:
                value = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                dp[i][j] = value + 1
    answer = 0
    for data in dp:
        answer = max(max(data),answer)
    answer *= answer
    return answer

b = [[0,0,1,1],[1,1,1,1]]
solution(b)
