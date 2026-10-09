def solution(sequence, k):
    answer = []
    cur_sum = 0
    min_len = 1000001
    l = 0
    for i in range(len(sequence)) :
        cur_sum += sequence[i]
        while cur_sum > k :
            cur_sum -= sequence[l]
            l += 1
        if cur_sum == k :
            if min_len > i - l + 1 :
                min_len = i - l + 1
                answer = [l, i]
    return answer