def solution(s):
    if len(s) % 2 == 1 :
        return False
    
    bracket_pair = {']':'[', '}':'{', ')': '('}
    st = []
    for c in s :
        if c in bracket_pair :
            if st :
                if st[-1] != bracket_pair[c] :
                    return False
                else :
                    st.pop()
            else :
                return False
        else :
            st.append(c)
    
    return False if st else True