# djikstra 각 정점에 대해서 수행해서 각 dist 값의 인덱스에 해당하는 거리합 최솟값 구하기, 거쳐가야 할 지점을 구할 필요x
from collections import defaultdict
import heapq
INF = float('inf')
def djikstra(n, graph, start) :
    pq = []
    heapq.heappush(pq, (0, start))
    dist = [INF] * (n+1)
    dist[start] = 0
    
    while pq :
        cur_cost, cur_dest = heapq.heappop(pq)
        if cur_cost > dist[cur_dest] :
            continue
        
        for next_cost, next_dest in graph[cur_dest] :
            new_cost = cur_cost + next_cost
            if new_cost < dist[next_dest] :
                dist[next_dest] = new_cost
                heapq.heappush(pq, (new_cost, next_dest))
    
    return dist[1:]
    
def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for u, v, cost in fares :
        graph[u].append((cost, v))
        graph[v].append((cost, u))
    
    from_s = djikstra(n, graph, s)
    from_a = djikstra(n, graph, a)
    from_b = djikstra(n, graph, b)
    
    answer = INF
    for i in range(n) :
        cost = from_s[i] + from_a[i] + from_b[i]
        answer = min(answer, cost)
            
    return answer