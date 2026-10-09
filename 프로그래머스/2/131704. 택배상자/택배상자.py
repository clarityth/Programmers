def solution(order):
    answer = 0
    st = []
    next_box = 1
    
    for o in order :
        while o > next_box :
            st.append(next_box)
            next_box += 1
            
        if o == next_box :
            answer += 1
            next_box += 1
        elif st and st[-1] == o :
            st.pop()
            answer += 1
        else :
            break
            
    return answer