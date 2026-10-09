from itertools import permutations
def solution(numbers):
    def isPrime(n) :
        if n <= 1 :
            return False
        for i in range(2, int(n**(0.5))+1) :
            if n % i == 0 :
                return False
        return True
    
    answer = 0
    num_set = set()
    
    for i in range(1, len(numbers)+1) :
        for j in permutations(numbers, i) :
            temp = ''.join(j)
            temp = temp.lstrip('0')
            if temp :
                num_set.add(temp)
            
    num_set = set(map(int, num_set))
    for num in num_set :
        if isPrime(num) :
            print(num)
            answer += 1

    return answer