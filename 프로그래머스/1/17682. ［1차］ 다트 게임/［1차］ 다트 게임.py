def solution(dartResult):
    idx = 0
    stack = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    while idx < len(dartResult) :
        num = ""
        
        while dartResult[idx].isdigit() : # 숫자 모으기
            num += dartResult[idx]
            idx += 1
        score = int(num)**bonus[dartResult[idx]] # 보너스 계산
        idx += 1
        
        if idx < len(dartResult) and dartResult[idx] in '*#' :
            if dartResult[idx] == '*' : # 스타상
                if stack :
                    score = score * 2
                    stack[-1] *= 2
                else :
                    score *= 2
            else : # 아차상
                score *= -1
            idx += 1
        stack.append(score)
                
    return sum(stack)