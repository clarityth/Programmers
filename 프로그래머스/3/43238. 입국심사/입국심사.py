def solution(n, times):
    answer = 0
    l = 1
    r = max(times) * n
    
    while l <= r :
        mid = (l+r) // 2
        processed = sum(mid // t for t in times)
        if processed < n :
        # 심사한 사람 수가 부족하면 시간을 더 늘려야 함
            l = mid + 1
        else :
        # 심사한 사람 수가 n명 이상이면 조건은 만족
            answer = mid # 정답을 미리 기록
            r = mid - 1 # 더 짧은 시간도 가능한지 범위를 줄임

    return answer