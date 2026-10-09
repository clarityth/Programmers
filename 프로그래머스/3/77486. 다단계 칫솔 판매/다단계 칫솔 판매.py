def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    name_dict = {name: i for i, name in enumerate(enroll)}
    referral_dict = {name: referrer for name, referrer in zip(enroll, referral)}
    
    for s, a in zip(seller, amount) :
        curr = s
        money = a*100
        
        while curr != '-' and money > 0 :
            pass_up = int(money*0.1)
            keep = money - pass_up
            
            answer[name_dict[curr]] += keep
            
            curr = referral_dict[curr]
            money = pass_up
            
    return answer