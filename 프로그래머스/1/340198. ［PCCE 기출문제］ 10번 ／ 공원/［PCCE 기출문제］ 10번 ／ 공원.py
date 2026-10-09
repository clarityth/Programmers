def solution(mats, park):
    mats.sort(reverse=True) # 큰 돗자리부터 확인
    col = len(park[0]) # 공원 가로
    row = len(park) # 공원 세로
    
    for size in mats : # 돗자리 크기별 확인
        for i in range(row - size + 1) : # 세로 범위 탐색
            for j in range(col - size + 1) : # 가로 범위 탐색
                if park[i][j] == "-1" : # 빈자리를 발견했다면
                    canPlace = True
                    for k in range(size) : # 가로 세로를 size만큼 이동하며 확인
                        for l in range(size) :
                            if park[i + k][j + l] != "-1" : # 배치하지 못한다면 탐색 중지
                                canPlace = False
                                break
                        if not canPlace : # 배치하지 못한다면 탐색 중지
                            break
                    if canPlace : # 배치가능하다면 바로 반환하여 가장 큰 돗자리 크기를 반환
                        return size            
    return -1