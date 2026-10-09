def solution(land):
    answer = 0
    
    n = len(land)
    dp = [[0]*4 for _ in range(n)]
    for i in range(len(land[0])) :
        dp[0][i] = land[0][i] 
    
    for i in range(1, n) :
        for j in range(4) :
            for k in range(4) :
                if j == k :
                    continue
                dp[i][j] = max(dp[i][j], dp[i-1][k])
            dp[i][j] += land[i][j]
            
    return max(dp[-1])