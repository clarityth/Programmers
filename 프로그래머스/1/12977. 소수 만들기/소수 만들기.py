def solution(nums):
    answer = 0
    isPrime = [True] * 3001
    isPrime[0] = isPrime[1] = 0
    
    for i in range(2, int(3001**0.5)) :
        for j in range(i*i, 3001, i) :
            isPrime[j] = False
    
    for i in range(0, len(nums) - 2) :
        for j in range(i + 1, len(nums) - 1) :
            for k in range(j + 1, len(nums)) :
                if isPrime[nums[i] + nums[j] + nums[k]] :
                    answer += 1
    return answer