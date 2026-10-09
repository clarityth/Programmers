def solution(A,B):
    answer = 0

    sorted_a = sorted(A)
    r_sorted_b = sorted(B, reverse=True)

    print(sorted_a[0])

    for i in range(len(A)) :
        answer += sorted_a[i] * r_sorted_b[i]
    
    return answer