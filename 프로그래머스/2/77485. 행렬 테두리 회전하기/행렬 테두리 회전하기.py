def solution(rows, columns, queries):
    answer = []
    grid = [[0]*columns for _ in range(rows)]
    n = 1
    for r in range(rows):
        for c in range(columns):
            grid[r][c] = n
            n += 1
            
    def rotate(grid, c1, r1, c2, r2):
        pos = []
        vals = []
        for c in range(c1, c2+1):
            pos.append((r1, c))
            vals.append(grid[r1][c])
            
        for r in range(r1+1, r2+1):
            pos.append((r, c2))
            vals.append(grid[r][c2])
        
        for c in range(c2-1, c1-1, -1):
            pos.append((r2, c))
            vals.append(grid[r2][c])
        
        for r in range(r2-1, r1, -1):
            pos.append((r, c1))
            vals.append((grid[r][c1]))
        
        pushed_vals = [vals[-1]] + vals[:-1]
        
        diff = []
        for i in range(len(vals)):
            if pushed_vals[i] != vals[i]:
                diff.append(pushed_vals[i])
            r, c = pos[i][0], pos[i][1]
            grid[r][c] = pushed_vals[i]

        return min(diff)

    for r1, c1, r2, c2 in queries:
        answer.append(rotate(grid, c1-1, r1-1, c2-1, r2-1))
        
    return answer