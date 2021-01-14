def solution(n):
    dp = [0]*(n+1)
    for i in range(n+1):
        if i <=1:
            dp[i] = i
        else:
            dp[i] = dp[i-1]+dp[i-2]
    answer = dp[n] % 1234567
    return answer