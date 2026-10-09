def solution(s):
    splitted_s = s.split()
    st = []
    for c in splitted_s :
        if c == 'Z' :
            st.pop()
        else :
            st.append(int(c))
    
    answer = 0
    while st :
        answer += st.pop()
        
    return answer