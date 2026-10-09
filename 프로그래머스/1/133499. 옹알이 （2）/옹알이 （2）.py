def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        prev = ""
        while word :
            found = False 
            for c in can :
                if word.startswith(c) : # 현재 잘라진 단어의 시작에서 말할 수 있는 단어를 찾음
                    if prev == c : # 연속된 발음이라면 실패
                        break
                    else : # 연속이 아니라면 말할 수 있는 단어를 자르고, prev 업데이트
                        prev = c
                        word = word[len(c):]
                        found = True
            if not found :
                break
        if not word :
            answer += 1
    return answer