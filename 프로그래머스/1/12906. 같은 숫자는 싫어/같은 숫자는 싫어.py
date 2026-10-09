def solution(arr):
    answer = []
    for a in arr :
        if answer :
            if answer[-1] != a :
                answer.append(a)
        else :
            answer.append(a)
    return answer