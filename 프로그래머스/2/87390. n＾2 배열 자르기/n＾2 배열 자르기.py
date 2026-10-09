def solution(n, left, right):
    answer = []
    for i in range(left, right+1) :
        div = i // n
        rest = i % n
        answer.append(max(div, rest) + 1)
    
    # n:3, l: 2, r: 5 
    # 1      2     {3[0,2] 
    # 2[1,0] 2[1,1] 3[1,2]} 
    # 3      3      3
    
    # n:4, l: 7, r: 14 
    # 1 2 3 4 / 2 2 3[1,2] {4[1,3] / 3[2,0] 3[2,1] 3[2,2] 4[2,3] / 4[3,0] 4[3,1] 4[3,2]} 4 
    # 1 2 3 4 5 / 2 2 3 4 5 / 3 3 3 4 5 / 4 4 4 4 5 / 5 5 5 5 5  
    return answer