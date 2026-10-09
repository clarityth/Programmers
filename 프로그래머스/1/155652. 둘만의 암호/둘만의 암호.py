def solution(s, skip, index):
    answer = ''
    skip_set = set(skip)
    for c in s :
        asc = ord(c) # 아스키 코드 변환            
        cnt = 0
        while cnt < index :
            asc += 1
            if asc > ord('z') : # z 초과시 a로 돌림
                asc = ord('a')
            if chr(asc) not in skip_set : # 현재 알파벳이 스킵에 포함되지 않았다면 카운트
                cnt += 1
        answer += chr(asc)
    return answer