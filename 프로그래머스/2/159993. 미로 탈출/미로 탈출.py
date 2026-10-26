from collections import deque
def solution(maps):
    answer = 0
    grid = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    start, exit = None, None
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            grid[r][c] = maps[r][c]
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                exit = (r, c)
                
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[False]*2 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[start[0]][start[1]][0] = True
    
    q = deque([(start[0], start[1], 0, 0)])
    while q:
        r, c, is_pulled, cnt = q.popleft()
        
        if is_pulled == 1 and (r, c) == exit:
            return cnt 
            
        for dr, dc in dir:
            n_r, n_c = r+dr, c+dc
            if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and not visited[n_r][n_c][is_pulled]:
                if grid[n_r][n_c] in ['S', 'O', 'E']:
                    q.append((n_r, n_c, is_pulled, cnt+1))
                    visited[n_r][n_c][is_pulled] = True
                    
                elif grid[n_r][n_c] == 'L':
                    q.append((n_r, n_c, 1, cnt+1))
                    visited[n_r][n_c][0] = True
                    visited[n_r][n_c][1] = True

    return -1