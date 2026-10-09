from collections import Counter
def solution(citations):
    sorted_cit = sorted(citations, reverse=True)
    # 6 5 3 1 0
    
    for i, c in enumerate(sorted_cit) :
        if c < i+1 :
            return i

    return len(citations)