def solution(n):
    answer = 0
    cols = set()
    diag1 = set() # 우상향 대각선
    diag2 = set() # 우하향 대각선
    
    def dfs(row) :
        nonlocal answer
        if row == n :
            answer += 1
            return
        
        for col in range(n) :
            if col in cols or (row+col) in diag1 or (row-col) in diag2 :
                continue
                
            cols.add(col)
            diag1.add(row+col)
            diag2.add(row-col)
            dfs(row+1)
            cols.remove(col)
            diag1.remove(row+col)
            diag2.remove(row-col)
    
    dfs(0)
    return answer