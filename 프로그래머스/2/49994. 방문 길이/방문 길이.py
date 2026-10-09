def solution(dirs):
    answer = 0
    pos = (0, 0)
    pos_set = set()
    
    for d in dirs :
        if d == 'U' :
            next_y = pos[1] + 1
            next_x = pos[0]
        elif d == 'D' :
            next_y = pos[1] - 1
            next_x = pos[0]
        elif d == 'R' :
            next_y = pos[1]
            next_x = pos[0] + 1
        elif d == 'L' :
            next_y = pos[1]
            next_x = pos[0] - 1
            
        next_pos = (next_x, next_y)
        
        if -5 <= next_y <= 5 and -5 <= next_x <= 5 :
            if (pos, next_pos) not in pos_set :
                pos_set.add((pos, next_pos))
                pos_set.add((next_pos, pos))
                answer += 1
            pos = next_pos
    return answer