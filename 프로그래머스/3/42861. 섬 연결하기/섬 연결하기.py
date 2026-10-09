from collections import defaultdict
import heapq

def kruskal(n, costs) :
    answer = 0
    costs.sort(key=lambda x: x[2]) # 간선 비용 오름차순 정렬
    
    parents = [i for i in range(n)] # 부모는 자기자신으로 초기화
    ranks = [0] * n # rank는 0으로 초기화
    
    def find(i) : # 재귀적으로 해당 노드의 부모를 찾음
        if parents[i] == i :
            return i
        parents[i] = find(parents[i])
        return parents[i]
    
    def union(a, b) : # 부모가 서로 다른 두 집합을 하나로 합침
        a_root = find(a)
        b_root = find(b)
        
        if a_root != b_root :
            if ranks[a_root] > ranks[b_root] : # rank가 작은 집합의 부모를 큰 집합 아래에 삽입
                parents[b_root] = a_root
            elif ranks[a_root] < ranks[b_root] :
                parents[a_root] = b_root
            else :
                ranks[a_root] += 1
                parents[b_root] = a_root
            
    for a, b, cost in costs : # 모든 간선을 비용이 적은 순으로 순회하며
        if find(a) != find(b) : # 두 집합의 부모가 다르다면 union 후 비용 합산
            answer += cost
            union(a, b)
    
    return answer

def prim(n, costs) :
    answer = 0
    graph = defaultdict(list)
    
    for a, b, cost in costs :
        graph[a].append((cost, b))
        graph[b].append((cost, a))
        
    pq = []
    heapq.heappush(pq, (0, 0)) # (cost, node)
    
    visited = set()
    
    while pq :
        cur_dist, cur_node = heapq.heappop(pq)
        
        if cur_node not in visited : # 우선순위 큐에서 꺼내자마자 방문/비용 처리 (bfs는 넣으면서 방문 처리)
            visited.add(cur_node)
            answer += cur_dist
            
            for next_dist, next_node in graph[cur_node] :
                if next_node not in visited :
                    heapq.heappush(pq, (next_dist, next_node))
    
    return answer

def solution(n, costs): # MST: kruskal or prim
    # return kruskal(n, costs)
    return prim(n, costs)