def solution(k, dungeons):
    answer = -1
    min_req_hp = min(dungeons[i][0] for i in range(len(dungeons)))
    
    def dfs(hp, cnt, visited) :
        nonlocal answer
        answer = max(answer, cnt)
        if hp < min_req_hp :
            return
        
        for i in range(len(dungeons)) :
            if i in visited :
                continue
                
            if dungeons[i][0] <= hp :
                visited.add(i)
                dfs(hp-dungeons[i][1], cnt+1, visited)
                visited.remove(i)
                
    dfs(k, 0, set())
    return answer