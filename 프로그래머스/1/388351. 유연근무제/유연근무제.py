def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(timelogs)) :
        isValid = True
        day = startday % 7
        des_tot_m = schedules[i] // 100 * 60 + (schedules[i] % 100)
        for j in range(len(timelogs[i])) :
            if day == 6 or day == 0:
                print("주말")
                day = (day + 1) % 7
                continue
                
            time = timelogs[i][j]
            tot_m = time // 100 * 60 + (time % 100)
            day = (day + 1) % 7
            
            if tot_m > des_tot_m + 10:
                isValid = False
                break
        if isValid :
            answer += 1
    return answer