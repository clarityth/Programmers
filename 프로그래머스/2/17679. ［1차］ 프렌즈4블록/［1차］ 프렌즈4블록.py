def solution(m, n, board):
    answer = 0
    
    grid = [[None]*n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            grid[r][c] = board[r][c]
            
    def gravity(grid):
        for c in range(n):
            st = []
            for r in range(m):
                if grid[r][c] != '0':
                    st.append(grid[r][c])
                    grid[r][c] = '0'
            
            t_r = m-1
            while st:
                grid[t_r][c] = st.pop()
                t_r -= 1
        
        return
        
    while True:
        removed = set()
        for r in range(m-1):
            for c in range(n-1):
                basis = grid[r][c]
                if grid[r][c] == '0':
                    continue

                if basis == grid[r+1][c] == grid[r+1][c+1] == grid[r][c+1]:
                    removed.add((r, c))
                    removed.add((r+1, c))
                    removed.add((r+1, c+1))
                    removed.add((r, c+1))
        
        if len(removed) > 0:
            answer += len(removed)
            for (r_r, r_c) in removed:
                grid[r_r][r_c] = '0'
            
            gravity(grid)
            
        else:
            break
            
    return answer