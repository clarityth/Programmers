def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(start, visited) :
        visited[start] = True
        for i, connected in enumerate(computers[start]) :
            if not visited[i] and connected:
                dfs(i, visited)
    
    for i in range(n) :
        if not visited[i] :
            dfs(i, visited)
            answer += 1
            
    return answer