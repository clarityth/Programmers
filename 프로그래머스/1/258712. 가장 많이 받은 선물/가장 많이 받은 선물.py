from collections import defaultdict
def solution(friends, gifts):
    gift_dict = defaultdict(int) # 선물을 주고 받은 내역
    give_cnts = defaultdict(int) # 준 선물 갯수
    receive_cnts = defaultdict(int) # 받은 선물 갯수
    next_mon_cnts = defaultdict(int) # 다음달 받을 선물 갯수
    
    for gift in gifts : # 전체 선물 내역에 대해
        giver, receiver = gift.split() 
        gift_dict[(giver, receiver)] += 1 # 주고 받은 내역
        give_cnts[giver] += 1 # 선물 준 갯수
        receive_cnts[receiver] += 1 # 선물 받은 갯수
        
    for i in range(len(friends)) : # 각 친구들을 순회
        for j in range(i + 1, len(friends)) :
            a = friends[i]
            b = friends[j]
            a_to_b = gift_dict[(a, b)] 
            b_to_a = gift_dict[(b, a)]
            
            if a_to_b > b_to_a : # a가 b에게 준 선물의 갯수가 더 많다면 a가 다음달에 받음
                next_mon_cnts[a] += 1
            
            elif a_to_b < b_to_a : # b가 a에게 준 선물의 갯수가 더 많다면 b가 다음달에 받음
                next_mon_cnts[b] += 1 
            
            else : # 두 사람의 선물의 갯수가 동일하거나 주고 받지 않았다면 선물 지수 비교
                a_score = give_cnts[a] - receive_cnts[a]
                b_score = give_cnts[b] - receive_cnts[b]
                
                if a_score > b_score : # a의 선물 지수가 더 크다면 a가 다음달에 받음
                    next_mon_cnts[a] += 1
                    
                elif a_score < b_score : # b의 선물 지수가 더 크다면 b가 다음달에 받음
                    next_mon_cnts[b] += 1
                    
    answer = max(next_mon_cnts.values(), default=0)
    return answer