from collections import defaultdict
import heapq

# djikstra: heapq, dist, defaultdict
def djikstra(N, road, K) :
    answer = 0
    graph = defaultdict(list)
    
    for a, b, cost in road :
        graph[a].append((cost, b)) # 양방향 간선
        graph[b].append((cost, a))
    
    INF = float('inf')
    dist = [INF] * (N+1) # 1-based index
    
    # 임의의 정점 1에서 시작
    dist[1] = 0
    
    pq = []
    heapq.heappush(pq, (0, 1)) # cost, node
    
    while pq :
        cur_dist, cur_node = heapq.heappop(pq)
        
        if cur_dist > dist[cur_node] :
            continue
        
        for next_dist, next_node in graph[cur_node] :
            new_dist = cur_dist + next_dist
            
            if dist[next_node] > new_dist :
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    for i in range(1, N+1) :
        if dist[i] <= K :
            answer += 1
            
    return answer

# bellmanford: edges, dist, INF 로직, 음수 싸이클
def bellmanford(N, road, K) :
    answer = 0
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[1] = 0
    
    for i in range(N) : # N번 만큼 반복
        for a, b, cost in road : # 모든 간선들을 순회
            # a 방문 기록이 있고, a를 거쳐 b를 가는 것이 기존에 기록된 b를 가는 비용보다 작다면 갱신
            if dist[a] != INF and dist[b] > dist[a] + cost : 
                dist[b] = dist[a] + cost
                if i == N-1 :
                    print("음수 사이클 존재")
            # 양방향이므로
            if dist[b] != INF and dist[a] > dist[b] + cost :
                dist[a] = dist[b] + cost
                if i == N-1 :
                    print("음수 사이클 존재")
    
    for i in range(1, N+1) :
        if dist[i] <= K :
            answer += 1
    
    return answer

# floydwarshall: k 루프 최외각, 2차원 dist(i로부터 j까지 가는 거리)
def floydwarshall(N, road, K) :
    answer = 0
    INF = float('inf')
    dist = [[INF] * (N+1) for _ in range(N+1)]
        
    for a, b, cost in road :
        dist[a][b] = min(dist[a][b], cost)
        dist[b][a] = min(dist[b][a], cost)
        
    for i in range(1, N+1) :
        dist[i][i] = 0

    for k in range(1, N+1) :
        for i in range(1, N+1) :
            for j in range(1, N+1) :
                if dist[i][j] > dist[i][k] + dist[k][j] :
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    for i in range(1, N+1) :
        if dist[i][i] < 0 :
            print("음수 싸이클 존재")
            return -1 
        
    for i in range(1, N+1):
        if dist[1][i] <= K:
            answer += 1
                
    return answer
    
def solution(N, road, K):
    # return djikstra(N, road, K)
    # return bellmanford(N, road, K)
    return floydwarshall(N, road, K)