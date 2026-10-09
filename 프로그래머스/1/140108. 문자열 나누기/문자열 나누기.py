def solution(s):
    answer = 0
    same, diff = 0, 0
    target = s[0]
    
    for i, c in enumerate(s) :
        if target == c :
            same += 1
        else :
            diff += 1
        if same == diff :
            answer += 1
            same = diff = 0
            if i + 1 < len(s) :
                target = s[i + 1]
        elif same != diff and i + 1 >= len(s) :
            answer += 1
    
    return answer