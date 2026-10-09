def solution(A, B):
    A.sort()
    B.sort()
    
    a = 0
    b = 0
    score = 0
    
    while a < len(A) and b < len(B) :
        if A[a] > B[b] :
            b += 1
        elif A[a] < B[b] :
            a += 1
            b += 1
            score += 1
        else :
            b += 1
            
    return score