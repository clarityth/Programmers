from collections import defaultdict

def solution(k, m, score):
    answer = 0
    cnts = defaultdict(int)
    for s in score :
        cnts[s] += 1
    
    upper_score_apple = 0
    for i in range(k, 0, -1) :
        apple = cnts[i]
        if upper_score_apple > 0 :
            apple += upper_score_apple
        complete_box = apple // m
        upper_score_apple = apple % m
        answer += complete_box * m * i
    return answer