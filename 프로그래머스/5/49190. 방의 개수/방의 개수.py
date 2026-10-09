# 방문, 이동 좌표 hashing + 스케일업 로직
def solution(arrows):
    answer = 0
    pos_dict = {0: (0, -1), 1: (1, -1), 2: (1, 0), 3: (1, 1), 4: (0, 1), 5: (-1, 1), 6: (-1, 0), 7: (-1, -1)} # dx, dy
    visited = set() # (y, x)
    visited.add((0, 0))
    path = set()
    y, x = 0, 0
    
    for a in arrows :
        # 스케일업: 화살표 명령어 1개당 2번씩 쪼개서 이동 (소수점 교차 방지)
        for _ in range(2) :
            next_y = y + pos_dict[a][1]
            next_x = x + pos_dict[a][0]

            if (next_y, next_x) in visited : # 이전에 방문한 적은 있지만
                if (y, x, next_y, next_x) not in path : # 해당 경로로 방문한 적은 없다면
                    answer += 1
                    path.add((y, x, next_y, next_x)) # 양방향 삽입
                    path.add((next_y, next_x, y, x))

            else :
                # 최초 방문 기록
                visited.add((next_y, next_x)) 
                path.add((y, x, next_y, next_x))
                path.add((next_y, next_x, y, x))

            y = next_y
            x = next_x
        
    return answer