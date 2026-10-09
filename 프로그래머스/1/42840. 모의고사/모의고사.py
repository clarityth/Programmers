def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i, a in enumerate(answers) :
        if pattern_1[i%5] == a :
            scores[0] += 1
        if pattern_2[i%8] == a :
            scores[1] += 1
        if pattern_3[i%10] == a:
            scores[2] += 1
    
    answer = []
    max_score = max(scores)
    for i, score in enumerate(scores) :
        if max_score == score :
            answer.append(i+1)
            
    return answer