def solution(n, t, m, p):
    answer = ''
    nums = []
    
    def to_base(num, n) :
        if num == 0 :
            return ['0']
        digits = []
        while num > 0 :
            remain = num % n
            if remain >= 10 :
                digits.append(chr(ord('A')+remain-10))
            else :
                digits.append(str(remain))
            num //= n
        return list(reversed(digits))
    
    for i in range(t*m) :
        nums.extend(to_base(i, n))
        
    count = 0
    for i in range(p-1, t*m, m) :
        answer += nums[i]
            
    return answer