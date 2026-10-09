def solution(n, info):
    answer = [-1]
    max_diff = 0
    
    def dfs(idx, remain, records) :
        nonlocal answer, max_diff
        if idx == 11 :
            if remain > 0 :
                records[10] += remain # 남은 화살이 있는 경우 0점에 전부 쏨
            # 점수 계산
            ryan_score = apeach_score = 0
            for i in range(11) :
                if info[i] < records[i] : # 라이언이 더 많이 맞췄다면 라이언 득점
                    ryan_score += 10 - i
                elif info[i] > records[i] >= 0 : # 어피치가 더 많이 맞췄거나 똑같이 맞췄다면 어피치 득점 (단, 1발 이상 맞춰야 함)
                    apeach_score += 10 - i
            diff = ryan_score - apeach_score
            
            if diff > 0 : # 라이언이 이겼을 때 
                if diff > max_diff : # 최대 점수차 갱신
                    max_diff = diff
                    answer = records[:]

                elif diff == max_diff : # 점수 차이가 같을 경우 가장 낮은 점수를 더 많이 맞춘 경우를 리턴
                    for i in range(10, -1, -1) : # 점수가 낮은 순으로 순회
                        if answer[i] < records[i] : # 더 낮은 점수를 많이 맞췄다면 갱신
                            answer = records[:]
                            break
                        elif answer[i] > records[i] : # 적게 맞췄다면 갱신 중단
                            break
                        
            records[10] -= remain
            return
        
        # 해당 점수를 획득하는 경우
        if remain > info[idx] :
            records[idx] = info[idx]+1
            dfs(idx+1, remain-info[idx]-1, records)

        # 해당 점수 획득을 포기하는 경우
        records[idx] = 0
        dfs(idx+1, remain, records)
        
    dfs(0, n, [0] * 11)
                
    return answer