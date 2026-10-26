from heapq import heappush, heappop, heapify
from copy import deepcopy
def solution(scoville, K):
    answer = 0
    scoville_mh = deepcopy(scoville)
    
    heapify(scoville_mh)
    while scoville_mh and len(scoville_mh) >= 2 and scoville_mh[0] < K:
        new_scoville = heappop(scoville_mh) + heappop(scoville_mh)*2
        heappush(scoville_mh, new_scoville)
        answer += 1
        
    if scoville_mh and scoville_mh[0] >= K:
        return answer
    else: 
        return -1