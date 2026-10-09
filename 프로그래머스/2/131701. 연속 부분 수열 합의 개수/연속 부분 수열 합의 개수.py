def solution(elements):
    answer = set()
    for i in range(len(elements)) : # startidx
        cur_sum = 0
        for j in range(len(elements)) : # startidx+idx
            cur_sum += elements[(i+j) % len(elements)]
            answer.add(cur_sum)
    return len(answer)