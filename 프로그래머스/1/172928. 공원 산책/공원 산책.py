def solution(park, routes):
    dirs = {
        "N" : (-1, 0),
        "W" : (0, -1),
        "E" : (0, 1),
        "S" : (1, 0)
    }
    
    # 시작 위치 찾기
    for i in range(len(park)) :
        for j in range(len(park[0])) :
            if park[i][j] == "S" :
                y = i
                x = j
    
    # 명령어 시뮬레이션
    for route in routes :
        d, s = route.split()
        s = int(s)
        isValid = True
        
        # 공원 벗어나는지 확인
        dy, dx = dirs[d]
        nextY = y + dy * s
        nextX = x + dx * s
        if not ((0 <= nextY < len(park)) and (0 <= nextX < len(park[0]))) :
            continue
            
        # 장애물 만나는지 확인
        for i in range(1, s + 1) :
            nextY = y + dy * i
            nextX = x + dx * i
            if park[nextY][nextX] == 'X' :
                isValid = False
                break
        
        # 공원 범위 안이고, 장애물이 없다면 이동
        if isValid :
            y = nextY
            x = nextX
            
    answer = [y, x]
    return answer