from collections import Counter
def solution(N, stages):
    challenge_count = Counter(stages)
    total = len(stages)
    
    answer = []
    
    for i in range(1, N+1) :
        if total == 0 :
            answer.append((i, 0))
        else :
            answer.append((i, challenge_count[i]/total))
        total -= challenge_count[i]
        
    answer.sort(key=lambda x: -x[1])
    return list(i[0] for i in answer)