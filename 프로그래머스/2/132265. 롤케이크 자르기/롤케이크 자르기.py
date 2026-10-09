from collections import Counter
def solution(topping):
    answer = 0
    part_1 = Counter(topping)
    part_2 = set()
    
    for t in topping :
        part_1[t] -= 1
        if part_1[t] == 0 :
            del part_1[t]
            
        part_2.add(t)

        if len(part_1) == len(part_2) :
            answer += 1
        
    return answer