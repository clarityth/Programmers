from collections import deque
# 시뮬레이션 수행
def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 크기가 bridge_length의 다리를 만듬
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    weight_sum = 0 # 무게 계산 부분합
    
    while bridge :
        answer += 1
        # 먼저 큐 배출
        pop_ele = bridge.popleft()
        if pop_ele > 0 :
            weight_sum -= pop_ele
        
        # 큐 유입
        if trucks :
            # 진입 가능 (무게 초과하지 않으면)
            if trucks[0] + weight_sum <= weight :
                truck = trucks.popleft()
                bridge.append(truck)
                weight_sum += truck
            # 진입 불가능
            else :
                bridge.append(0)
            
    return answer