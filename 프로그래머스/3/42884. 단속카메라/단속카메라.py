def solution(routes):
    routes.sort(key=lambda x:x[1])
    answer = 1
    camera = routes[0][1]
    
    for i in range(1, len(routes)) :
        cur_start = routes[i][0]
        cur_end = routes[i][1]
        
        if cur_start <= camera <= cur_end :
            continue
        else :
            camera = cur_end
            answer += 1
        
    return answer 