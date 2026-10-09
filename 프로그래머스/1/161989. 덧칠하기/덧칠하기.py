def solution(n, m, section):
    answer = 1
    start_section = section[0]
    
    for i in range(1, len(section)) :
        if section[i] > start_section + m - 1: # 칠할 수 있는 범위 밖이라면 새로 칠함
            start_section = section[i]
            answer += 1
    return answer