from collections import defaultdict
from heapq import heappush, heappop

def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    def djikstra(start):
        dist = [float('inf')]*(N+1)
        pq = [(0, 1)]
        dist[start] = 0
        
        while pq:
            cost, dest = heappop(pq)
            
            if dist[dest] < cost:
                continue
            
            for next_cost, next_dest in graph[dest]:
                new_cost = cost+next_cost
                if dist[next_dest] > new_cost:
                    dist[next_dest] = new_cost
                    heappush(pq, (new_cost, next_dest))
        return dist
    
    dist = djikstra(1)
    for d in dist:
        if d <= K:
            answer += 1
            
    return answer