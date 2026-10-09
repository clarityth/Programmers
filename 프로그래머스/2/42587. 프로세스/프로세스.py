from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for i, p in enumerate(priorities) :
        q.append([p, location == i])
    
    while q :
        max_p = max(p for p, _ in q)
                
        if max_p > q[0][0] :
            q.append(q.popleft())
        
        else :
            answer += 1
            if q[0][1] :
                return answer
            q.popleft()
            
    return answer