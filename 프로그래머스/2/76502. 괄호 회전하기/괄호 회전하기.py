def solution(s):
    if len(s) % 2 == 1 : # 홀수 개라면 조합이 성립 불가능
        return 0
    
    bracket_pair = {')' : '(', '}' : '{', ']' : '['}
    answer = 0
        
    # 회전 칸 수
    for i in range(len(s)) :
        rotated_s = s[i:] + s[:i] # 회전 구현: 슬라이싱으로 시간 단축
            
        st = []
        is_valid = True
        for c in rotated_s : 
            if c not in bracket_pair : # 여는 괄호면 push
                st.append(c)
            else : # 닫는 괄호면
                if not st : # 스택이 비어있으면 만들 수 없음
                    is_valid = False
                    break
                if st[-1] == bracket_pair[c] :
                    st.pop()
                else :
                    is_valid = False
                    break
        if is_valid and not st : # 끝까지 진행했고, 스택에 원소가 남아있지 않다면
            answer += 1

    return answer