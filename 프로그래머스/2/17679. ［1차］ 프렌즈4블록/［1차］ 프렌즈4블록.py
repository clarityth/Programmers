def solution(m, n, board):
    
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    patterns = [[0, 1, 7], [1, 2, 3], [3, 4, 5], [5, 6, 7]]
    ans = 0
    
    grid = [[None]*n for _ in range(m)]

    for i in range(len(board)):
        for j in range(len(board[0])):
            grid[i][j] = board[i][j]
    
    while True:
        removed = set()
        is_removed = False
        for r in range(m):
            for c in range(n):
                basis = grid[r][c]
                if basis == '0':
                    continue
                    
                for i in range(4):
                    pat_removed = set()
                    pat_removed.add((r, c))
                    
                    for idx in patterns[i]:
                        dr, dc = dirs[idx][0], dirs[idx][1]
                        n_r, n_c = r+dr, c+dc

                        if 0 <= n_r < m and 0 <= n_c < n and grid[n_r][n_c] == basis:
                            pat_removed.add((n_r, n_c))

                        else:
                            break 

                    if len(pat_removed) == 4:
                        removed |= pat_removed
                        is_removed = True
        
        if not is_removed:
            break
            
        for rr, rc in removed:
            grid[rr][rc] = '0'

        gravity(grid)
        ans += len(removed)
        
    return ans

def gravity(grid):
    for c in range(len(grid[0])):
        st = []
        for r in range(len(grid)):
            if grid[r][c] != '0':
                st.append(grid[r][c])
                grid[r][c] = '0'

        tar_r = len(grid)-1
        while st:
            grid[tar_r][c] = st.pop()
            tar_r -= 1