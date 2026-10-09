def solution(name, yearning, photo):
    answer = []
    scores = {n: y for n, y in zip(name, yearning)}
    for p in photo :
        total = sum(scores.get(person, 0) for person in p)
        answer.append(total)
        
    return answer