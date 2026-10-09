def parsetime(input) :
    m, s = map(int, input.split(":"))
    return m * 60 + s
    
def solution(video_len, pos, op_start, op_end, commands):
    tot_len = parsetime(video_len)
    cur_pos = parsetime(pos)
    start_op = parsetime(op_start)
    end_op = parsetime(op_end)
    
    for c in commands :
        if start_op <= cur_pos <= end_op : # 오프닝 구간 체크
            cur_pos = end_op
            
        if c == "next" :
            cur_pos += 10
            
        elif c == "prev" :
            cur_pos -= 10
            
        if start_op <= cur_pos <= end_op : # 오프닝 구간 체크
            cur_pos = end_op
            
        if cur_pos < 0 : # 최소 길이 미만
            cur_pos = 0
        
        if cur_pos >= tot_len : # 전체 길이 초과
            cur_pos = tot_len
            
    answer = f"{cur_pos//60:02}:{cur_pos % 60:02}"
    return answer