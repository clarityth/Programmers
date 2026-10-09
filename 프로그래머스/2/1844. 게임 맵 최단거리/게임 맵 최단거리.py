from collections import deque
def solution(maps):
    n = len(maps[0])
    m = len(maps)
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    q = deque([((0, 0), 1)])
    
    while q :
        (cur_y, cur_x), cnt = q.popleft()
        
        if (cur_y, cur_x) == (m-1, n-1) :
            return cnt
        
        for i in range(4) :
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if 0 <= next_x < n and 0 <= next_y < m and maps[next_y][next_x] != 0 and not visited[next_y][next_x] :
                visited[next_y][next_x] = True
                q.append(((next_y, next_x), cnt + 1))
        
    return -1