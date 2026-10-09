def solution(n, k):
    answer = 0
    def to_base(n, k) :
        digits = []
        while n > 0 :
            digits.append(str(n % k))
            n //= k
        return ''.join(reversed(digits))
    
    def is_prime(n) :
        if n == 0 or n == 1 :
            return False
        for i in range(2, int(n**0.5)+1) :
            if n % i == 0 :
                return False
        return True
    
    k_digit = to_base(n, k)
    candidates = k_digit.split('0')
    for c in candidates :
        if c and is_prime(int(c)) :
            answer += 1
    return answer