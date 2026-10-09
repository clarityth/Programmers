from collections import deque
def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for (parent, child) in edges :
        graph[parent].append(child)
    
    max_sheep = 1
    q = deque([(0, 1, 0, set())])
    
    while q :
        cur_node, sheep, wolf, next_nodes = q.popleft()
        max_sheep = max(max_sheep, sheep)
        next_nodes.update(graph[cur_node])
        
        for next_node in next_nodes :
            if info[next_node] == 0 : # 양
                q.append((next_node, sheep+1, wolf, next_nodes - {next_node}))
            else : # 늑대
                if sheep > wolf+1 :
                    q.append((next_node, sheep, wolf+1, next_nodes - {next_node}))
                
    return max_sheep