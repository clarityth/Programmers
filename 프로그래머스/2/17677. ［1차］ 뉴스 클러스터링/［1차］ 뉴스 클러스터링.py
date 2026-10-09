from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    set_1 = []
    set_2 = []
    
    for i in range(0, len(str1)-1) :
        if i+1 < len(str1) :
            candidate = str1[i:i+2]
            if candidate.isalpha() :
                set_1.append(candidate)
                
    for i in range(0, len(str2)-1) :
        if i+1 < len(str2) :
            candidate = str2[i:i+2]
            if candidate.isalpha() :
                set_2.append(candidate)
                
    if len(set_1) == 0 and len(set_2) == 0:
        return 65536
    
    count1 = Counter(set_1)
    count2 = Counter(set_2)
    
    sum_count = sum((count1 | count2).values())
    inter_count = sum((count1 & count2).values())

    answer = int((inter_count / sum_count) * 65536)
        
    return answer