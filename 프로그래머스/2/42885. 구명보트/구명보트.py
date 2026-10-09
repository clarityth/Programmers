def solution(people, limit):
    sorted_p = sorted(people, reverse=True)
    answer = 0
    i, j = 0, len(sorted_p)-1
    
    while i <= j :
        if sorted_p[i] + sorted_p[j] <= limit :
            j -= 1
        i += 1
        answer += 1
    return answer