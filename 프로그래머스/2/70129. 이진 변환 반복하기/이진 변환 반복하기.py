def solution(s):
    answer = [0, 0]
    
    while s != '1' :
        answer[0] += 1
        
        zero_cnt = s.count('0')
        answer[1] += zero_cnt
        
        length = len(s) - zero_cnt
        
        temp = []
        while length > 0 :
            temp.append(str(length % 2))
            length //= 2
            
        s = ''.join(temp[::-1])
            
    return answer