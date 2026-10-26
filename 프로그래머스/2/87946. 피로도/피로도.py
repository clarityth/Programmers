def solution(k, dungeons):
    answer = 0
    
    def dfs(depth, visited, hp):
        nonlocal answer
        
        answer = max(answer, len(visited))
        
        for i in range(len(dungeons)):
            if i in visited:
                continue
                
            if dungeons[i][0] <= hp:
                visited.add(i)
                dfs(depth+1, visited, hp - dungeons[i][1])
                visited.remove(i)
                
    dfs(0, set(), k)
    return answer