def solution(n, k, cmd):
    up_down = [[i-1, i+1] for i in range(n)]
    up_down[0][0] = None
    up_down[n-1][1] = None
    cursor = k
    deleted = []
    for c in cmd : 
        splitted_c = c.split()
        
        if len(splitted_c) == 2 : # 커서 이동
            operator = splitted_c[0]
            operand = int(splitted_c[1])
            
            if operator == 'U' : # 커서 위로 이동
                while operand > 0 :
                    operand -= 1
                    cursor = up_down[cursor][0]
            else : # 커서 아래로 이동
                while operand > 0 :
                    operand -= 1
                    cursor = up_down[cursor][1]

        else :
            operator = splitted_c[0]
            
            if operator == 'C' :
                before = up_down[cursor][0]
                after = up_down[cursor][1]
                deleted.append((cursor, before, after)) # 현재 선택된 행을 삭제
                
                # 링크드리스트 연결 끊기
                if before is not None :
                    up_down[before][1] = after
                if after is not None :
                    up_down[after][0] = before
                
                # 커서 이동
                if after is None : # 삭제한 행이 마지막 행인 경우 이전 행 선택
                    cursor = before
                else : # 일반의 경우, 다음 행 선택
                    cursor = after
            
            # 최근 삭제 행 복구
            elif operator == 'Z' :
                idx, before, after = deleted.pop()
                # 링크드리스트 재연결
                if before is not None :
                    up_down[before][1] = idx
                if after is not None :
                    up_down[after][0] = idx
                    
    answer = ['O'] * n
    while deleted :
        answer[deleted.pop()[0]] = 'X'
        
    return ''.join(answer[i] for i in range(n))