import heapq
def solution(operations):
    min_h = []
    max_h = []
    count = {}
    
    for ops in operations :
        o, v = ops.split()
        v = int(v)
        if o == 'I' :
            heapq.heappush(min_h, v)
            heapq.heappush(max_h, -v)
            count.setdefault(v, 0)
            count[v] += 1
            
        else :
            if v == 1: #최댓값 삭제
                while max_h and count[-max_h[0]] == 0 :
                    heapq.heappop(max_h)
                if max_h :
                    d_v = -heapq.heappop(max_h)
                    count[d_v] -= 1
                
            else : #최솟값 삭제
                while min_h and count[min_h[0]] == 0 :
                    heapq.heappop(min_h)
                if min_h :
                    d_v = heapq.heappop(min_h)
                    count[d_v] -= 1
    
    while min_h and count[min_h[0]] == 0 :
        heapq.heappop(min_h)
    while max_h and count[-max_h[0]] == 0 :
        heapq.heappop(max_h)
        
    if min_h and max_h :  
        return [-max_h[0], min_h[0]]
    
    return [0, 0]