def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    p_set = set((j-1, i-1) for i, j in puddles)
    
    for i in range(n) :
        for j in range(m) :
            if (i, j) not in p_set :
                if 0 <= i-1 :
                    dp[i][j] += dp[i-1][j] % 1000000007

                if 0 <= j-1 :
                    dp[i][j] += dp[i][j-1] % 1000000007

    return dp[n-1][m-1] % 1000000007