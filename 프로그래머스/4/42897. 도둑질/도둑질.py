def rob(arr) :
    dp = [[0]*2 for _ in range(len(arr))]
    dp[0][1] = arr[0]
    
    for i in range(1, len(arr)) :
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0] + arr[i]
    
    return max(dp[i])

def solution(money):
    return max(rob(money[1:]), rob(money[:-1]))