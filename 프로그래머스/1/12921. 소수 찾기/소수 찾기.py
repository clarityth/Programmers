def solution(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(n**0.5) + 1) :
        for j in range(i*i, n + 1, i) :
            isPrime[j] = False
    answer = sum(isPrime)
    return answer