from collections import defaultdict
def solution(survey, choices):
    answer = ''
    score = defaultdict(int)
    for i in range(len(survey)) :
        a = survey[i][0]
        b = survey[i][1]

        if choices[i] > 4 : # b를 선택
            score[b] += choices[i] - 4
        elif choices[i] < 4 : # a를 선택
            score[a] += 4 - choices[i]
    
    types = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    for a, b in types :
        if score[a] > score[b] :
            answer += a
        elif score[a] < score[b] :
            answer += b
        else :
            answer += min(a, b)
    return answer