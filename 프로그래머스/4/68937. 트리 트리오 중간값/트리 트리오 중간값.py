from collections import defaultdict, deque
def solution(n, edges):
    con_dict = defaultdict(list)
    for (a, b) in edges :
        con_dict[a].append(b)
        con_dict[b].append(a)
    
    def bfs(start) :
        max_cnt = 0
        max_nodes = []
        q = deque([(start, 0, set([start]))])
        
        while q :
            cur_node, cnt, visited = q.popleft()
            if cnt > max_cnt :
                max_cnt = cnt
                max_nodes = [cur_node]
                
            elif cnt == max_cnt :
                max_nodes.append(cur_node)
                
            for nxt_node in con_dict[cur_node] :
                if nxt_node not in visited :
                    visited.add(nxt_node)
                    q.append((nxt_node, cnt+1, visited))
        return (max_cnt, max_nodes)
    
    _, node_1 = bfs(2) # 임의의 점에서 가장 멀리 있는 노드 하나를 찾음
    f_max_cnt, f_max_nodes = bfs(node_1[0]) # 해당 노드에서 bfs 수행해서 가장 먼 거리에 있는 노드들을 찾음
    if len(f_max_nodes) >= 2 : # 만약 가장 먼 거리에 있는 노드가 2개 이상이라면 중간 거리 = 노드의 지름
        return f_max_cnt
    else : # 1개라면 bfs 재수행
        s_max_cnt, s_max_nodes = bfs(f_max_nodes[0]) # 해당 점에서 bfs를 다시 수행
        if len(s_max_nodes) >= 2 : # 가장 먼 거리에 있는 노드가 2개 이상이라면 중간 거리 = 노드의 지름
            return s_max_cnt
        else : # 1개라면 거리-1
            return s_max_cnt - 1
    return -1