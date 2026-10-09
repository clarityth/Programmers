from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    answer = len(dist) + 1
    for i in range(length) :
        weak.append(weak[i]+n)
    
    for i in range(length) :
        for friends in permutations(dist, len(dist)) :
            cnt = 1
            pos = weak[i] + friends[cnt-1]
            
            for j in range(i, i+length) :
                if pos < weak[j] :
                    cnt += 1
                
                    if cnt > len(dist) :
                        break
                
                    pos = weak[j] + friends[cnt-1]
            
            if cnt <= len(dist) :
                answer = min(answer, cnt)
            
    return answer if answer != len(dist)+1 else -1