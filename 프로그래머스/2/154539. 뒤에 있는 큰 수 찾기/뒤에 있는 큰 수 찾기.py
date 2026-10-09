def solution(numbers):
    answer = [-1] * len(numbers)
    st = []
    for i, num in enumerate(numbers) :
        while st and numbers[st[-1]] < num :
            idx = st.pop()
            answer[idx] = num
        st.append(i)
    return answer