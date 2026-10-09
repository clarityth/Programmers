# bfs + 3차원 거리 배열(이전 접근 방향, 가로, 세로)
from collections import deque
def solution(board):
    N = len(board)
    INF = float('inf')
    answer = 0
    costs = [[[INF] * 4 for _ in range(N)] for _ in range(N)] # [접근 방향][가로][세로]
    for i in range(4) :
        costs[0][0][i] = 100
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    
    # 초기 큐 상태: [0][0]에서 우측, 아래 방향으로 이동하는 경우
    if board[0][1] != 1 :
        q.append(((0, 1), 3, 100)) # 현재 좌표, 이전 접근 방향(상:0, 하:1, 좌:2, 우:3), 누적 비용
        costs[0][1][3] = 100
        
    if board[1][0] != 1 :
        q.append(((1, 0), 1, 100))
        costs[1][0][1] = 100
        
    while q :
        (cur_y, cur_x), prev_dir, cur_cost = q.popleft()
        if (cur_y, cur_x) == (N-1, N-1) :
            continue
        
        for i in range(4) :
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            cur_dir = i
            
            if 0 <= next_y < N and 0 <= next_x < N :
                if cur_dir != prev_dir : # 왼-오, 상-하가 연속되는 일은 bfs 로직에 의해 없음
                    next_cost = cur_cost + 600
                else :
                    next_cost = cur_cost + 100
                    
                if board[next_y][next_x] != 1 and costs[next_y][next_x][cur_dir] > next_cost :
                    costs[next_y][next_x][cur_dir] = next_cost
                    q.append(((next_y, next_x), cur_dir, next_cost))
        
    return min(costs[N-1][N-1])