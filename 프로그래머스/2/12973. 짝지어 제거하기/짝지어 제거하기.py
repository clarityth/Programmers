def solution(s):
    st = []
    for c in s :
        if not st :
            st.append(c)
        else :
            if st[-1] == c :
                st.pop()
            else :
                st.append(c)
    return 0 if st else 1