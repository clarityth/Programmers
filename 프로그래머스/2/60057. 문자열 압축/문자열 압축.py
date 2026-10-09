def solution(s):
    if len(s) == 1 :
        return 1
    answer = 1001
    
    for size in range(1, len(s)//2+1) :
        prev = s[:size]
        cnt = 1
        comp = ""
        for i in range(size, len(s), size) :
            cur = s[i:i+size]
            if prev == cur :
                cnt += 1
            else :
                comp += str(cnt if cnt > 1 else "") + prev
                cnt = 1
                prev = cur
                
        comp += str(cnt if cnt > 1 else "") + prev
        answer = min(answer, len(comp))
    return answer