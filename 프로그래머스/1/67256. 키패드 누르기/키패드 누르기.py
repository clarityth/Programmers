from collections import defaultdict

def solution(numbers, hand):
    answer = []
    
    left_pos = (3, 0)
    right_pos = (3, 2)
    
    keypad = defaultdict()
    num = 1
    for i in range(3) :
        for j in range(3) :
            keypad[num] = (i, j)
            num += 1
    keypad[0] = (3, 1)
    
    for number in numbers :
        if number in [1, 4, 7] :
            answer.append('L')
            left_pos = keypad[number]
        
        elif number in [3, 6, 9] :
            answer.append('R')
            right_pos = keypad[number]
            
        elif number in [2, 5, 8, 0] :
            num_pos = keypad[number]
            left_dist = abs(left_pos[0]-num_pos[0]) + abs(left_pos[1]-num_pos[1])
            right_dist = abs(right_pos[0]-num_pos[0]) + abs(right_pos[1]-num_pos[1])
            
            if left_dist < right_dist :
                answer.append('L')
                left_pos = num_pos
                
            elif left_dist > right_dist :
                answer.append('R')
                right_pos = num_pos
                
            else :
                if hand == 'right' :
                    answer.append('R')
                    right_pos = num_pos
                    
                else :
                    answer.append('L')
                    left_pos = num_pos
        
    return ''.join(answer)