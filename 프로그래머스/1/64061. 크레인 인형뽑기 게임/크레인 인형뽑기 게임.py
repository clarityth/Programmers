def solution(board, moves):
    answer = 0
    
    # 1. 2차원 보드를 열(Column) 단위의 스택 배열로 변환
    stacks = [[] for _ in range(len(board))]
    
    # 바닥(N-1)부터 탐색해 스택에 넣음으로써, 배열의 끝(Top)이 보드의 맨 위 인형이 되도록 세팅
    for i in range(len(board)-1, -1, -1) :
        for j in range(len(board[0])) :
            if board[i][j] != 0 :
                stacks[j].append(board[i][j])
    
    st = []
    
    # 2. 크레인 이동 및 인형 뽑기
    for m in moves :
        # 빈 열이 아닐 때만 크레인 작동
        if stacks[m-1] :
            picked = stacks[m-1].pop()
            
            # 바구니에 인형이 있고, 방금 뽑은 인형과 같다면 터트림
            if st and st[-1] == picked :
                answer += 2
                st.pop()
            else :
                st.append(picked)
                
    return answer