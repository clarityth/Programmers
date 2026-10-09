def solution(n, stations, w):
    answer = 0
    
    start = 1
    for station in stations :
        between_cnt = max(0, station-w-start)
        answer += between_cnt // (2*w+1)
        if between_cnt % (2*w+1) != 0 :
            answer += 1
        start = station+w+1
        
    if start <= n :
        between_cnt = max(0, n-start+1)
        answer += between_cnt // (2*w+1)
        if between_cnt % (2*w+1) != 0 :
            answer += 1

    return answer