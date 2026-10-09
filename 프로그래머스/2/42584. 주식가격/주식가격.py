def solution(prices):
    answer = [0] * len(prices)
    st = []
    
    for idx, price in enumerate(prices) :
        while st and prices[st[-1]] > price : # 스택 내부를 값 기준 비내림차순으로 정렬하되, 저장하는 값은 인덱스
            prev_idx = st.pop()
            answer[prev_idx] = idx - prev_idx # 가격이 떨어졌다면 해당 인덱스가 가격이 떨어지지 않은 시간을 계산하여 저장
        st.append(idx)
        
    while st : # 끝까지 떨어지지 않은 가격들의 인덱스가 담겨있음
        idx = st.pop()
        answer[idx] = len(prices) - 1 - idx
    return answer