from collections import defaultdict
def solution(n, wires):
    answer = n
    
    graph = defaultdict(list)
    for a, b in wires :
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(node, parent) :
        nonlocal answer
        sub_tree_cnt = 1
        
        for child in graph[node] :
            if child != parent :
                sub_tree_cnt += dfs(child, node)
                
        diff = abs(sub_tree_cnt-1*(n-sub_tree_cnt))
        answer = min(answer, diff)
        
        return sub_tree_cnt
    
    dfs(1, -1)
    return answer