from collections import defaultdict
def solution(gems):
    kind_cnt = len(set(gems))
    l = 0
    answer = [0, len(gems) - 1]
    
    counter = defaultdict(int)
    for r in range(len(gems)) :
        counter[gems[r]] += 1
        
        while len(counter) == kind_cnt :
            if answer[1] - answer[0] > r - l :
                answer = [l, r]
            
            counter[gems[l]] -= 1
            if counter[gems[l]] == 0 :
                del counter[gems[l]]
            l += 1
    return [answer[0] + 1, answer[1] + 1]