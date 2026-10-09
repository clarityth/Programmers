def solution(msg):
    answer = []
    dictionary = {}
    next_idx = 27
    for i in range(0, 26) :
        dictionary[chr(ord('A')+i)] = i+1
    
    start = 0
    while start < len(msg) :
        end = start + 1
        # 문자열 인덱스 범위를 넘어서지 않으면서 사전에 존재하는 가장 긴 인덱스의 범위를 구함
        while end <= len(msg) and msg[start:end] in dictionary :
            end += 1
            
        # 현재 입력 확정 (start:end-1까지가 사전에 등록된 유효한 입력)
        w = msg[start:end-1]
        answer.append(dictionary[w])
        
        # 처리되지 않은 글자가 있다면 신규 단어 등록
        if end <= len(msg) :
            dictionary[msg[start:end]] = next_idx
            next_idx += 1
        
        # 현재 입력 길이만큼 건너뜀
        start += len(w)

    return answer