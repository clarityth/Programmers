from collections import Counter
def solution(k, tangerine):
    cnts = Counter(tangerine)
    sorted_cnts = sorted(cnts.values())
    
    remain = len(tangerine) - k
    answer = len(sorted_cnts)
    
    for cnt in sorted_cnts :
        if remain >= cnt :
            answer -= 1
            remain -= cnt
            
        else :
            break
    return answer