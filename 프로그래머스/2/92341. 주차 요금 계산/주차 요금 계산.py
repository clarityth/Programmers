from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    car_dict = defaultdict(list)
    
    for record in records :
        time, car_num, info = record.split()
        hour, minute = map(int, time.split(':'))
        car_dict[car_num].append((info, hour * 60 + minute))    
    
    for car_num in sorted(car_dict.keys()) :
        st = []
        fee = 0
        tot_parking_min = 0
        
        for data in car_dict[car_num] :
            cur_info = data[0]
            cur_minute = data[1]
            
            if cur_info == 'IN' :
                st.append(cur_minute)
                
            elif cur_info == 'OUT' :
                if st :
                    prev_minute = st.pop()                    
                    tot_parking_min += cur_minute - prev_minute
        
        if st : # 23:59 출차 간주
            prev_minute = st.pop()
            tot_parking_min += 23*60+59 - prev_minute

        if tot_parking_min <= fees[0] :
            fee += fees[1]
        else :
            fee += fees[1]
            tot_parking_min -= fees[0]
            fee += math.ceil(tot_parking_min/fees[2])*fees[3]
            
        answer.append(fee)
        
    return answer