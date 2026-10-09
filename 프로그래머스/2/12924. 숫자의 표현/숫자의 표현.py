def solution(n):
    if n <= 2:
        return 1
    
    answer = 1
    dp = [0] * (n//2 + 2)
    dp[1] = 1
    for i in range(2, len(dp)) :
        dp[i] = i + dp[i-1]

    for i in range(1, len(dp)) :
        if dp[i] == n :
            answer += 1
            continue
            
        for j in range(i + 1, len(dp)) :
            dif = dp[j] - dp[i]

            if dif == n :
                answer += 1
                
            elif dif > n :
                break
    return answer