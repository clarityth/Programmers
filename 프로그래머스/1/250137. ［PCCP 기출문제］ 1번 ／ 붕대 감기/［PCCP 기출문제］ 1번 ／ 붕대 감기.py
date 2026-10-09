def solution(bandage, health, attacks):
    answer = health
    t, r, e = bandage
    b_cnt = 0
    attack_idx = 0
    
    for i in range (1, attacks[-1][0] + 1) :
        if attacks[attack_idx][0] == i : # 해당 시간에 공격이 들어왔을 경우
            b_cnt = 0
            answer -= attacks[attack_idx][1]
            if answer <= 0 : # 죽었을 경우
                return -1
            attack_idx += 1
            
        else :
            b_cnt += 1
            answer = min(answer + r, health) # 최대 체력 넘지 않도록
            if b_cnt == t : # 시전 시간에 도달했을 때 추가 회복
                answer = min(answer + e, health) # 최대 체력 넘지 않도록
                b_cnt = 0
                
        print(f"{i}초 : {answer}")
    return answer