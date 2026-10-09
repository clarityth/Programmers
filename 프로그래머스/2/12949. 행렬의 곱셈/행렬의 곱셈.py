def solution(arr1, arr2):
    # 1 4    3 3 
    # 3 2    3 3
    # 4 1
    r_1, c_1 = len(arr1), len(arr1[0])
    r_2, c_2 = len(arr2), len(arr2[0])
    
    answer = [[0]* c_2 for _ in range(r_1)]
    
    for i in range(r_1) :
        for j in range(c_2) :
            for k in range(c_1) :
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer