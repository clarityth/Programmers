# bfs 최대값/카운트 갱신
from collections import defaultdict, deque
def solution(n, edge):
    answer = 0
    max_dist = 0
    graph = defaultdict(list)
    for a, b in edge :
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([(1, 0)]) # 현재 노드, 이동 거리
    visited = set()
    visited.add(1)
    
    while q :
        cur_node, cur_dist = q.popleft()
        if max_dist < cur_dist :
            max_dist = cur_dist
            answer = 1
            
        elif max_dist == cur_dist :
            answer += 1

        for next_node in graph[cur_node] :
            if next_node not in visited :
                q.append((next_node, cur_dist+1))
                visited.add(next_node)
                
    return answer 