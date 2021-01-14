import copy

def hopscotch(board, size):
    result = 0
    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는?
    for i in range(1,size):
        for j in range(4):
            temp = copy.deepcopy(board[i-1])
            temp[j] = 0
            board[i][j]+=max(temp)
    result = max(board[-1])
    return result
board = [[3, 5, 6, 8], [3, 5, 3, 4], [5, 10, 4, 3], [1, 3000, 2, 1]]
print(hopscotch(board, 3))

def solution(land):
    N = len(land)
    dp = [[0]*4 for _ in range(N)]
    dp[0] = land[0]
    for i in range(1,N):
        for j in range(4):
            for k in range(4):
                if j != k:
                    dp[i][j] = max(dp[i][j],dp[i-1][k]+land[i][j])
    print(dp)
    answer = max(dp[N-1])
    return answer
l = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(board))