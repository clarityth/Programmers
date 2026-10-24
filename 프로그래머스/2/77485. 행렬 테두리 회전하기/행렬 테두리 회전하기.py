from copy import deepcopy
def solution(rows, columns, queries):
    answer = []
    grid = [[0]*columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = n
            n += 1
    
    def rotate(grid, l_r, l_c, r_r, r_c):
        overflows = (grid[l_r][r_c], grid[r_r][r_c], grid[r_r][l_c])
        
        for c in range(r_c, l_c-1, -1):
            grid[l_r][c] = grid[l_r][c-1]
        
        for r in range(r_r, l_r, -1):
            grid[r][r_c] = grid[r-1][r_c]
        
        for c in range(l_c, r_c):
            grid[r_r][c] = grid[r_r][c+1]
        
        for r in range(l_r, r_r):
            grid[r][l_c] = grid[r+1][l_c]
        
        grid[l_r+1][r_c] = overflows[0]
        grid[r_r][r_c-1] = overflows[1]
        grid[r_r-1][l_c] = overflows[2]
        

    for a, b, c, d in queries:
        basis = deepcopy(grid)
        rotate(grid, a-1, b-1, c-1, d-1)
        temp = []
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] != basis[r][c]:
                    temp.append((grid[r][c]))
        answer.append(min(temp))

    return answer