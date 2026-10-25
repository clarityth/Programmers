from collections import defaultdict

def solution(points, routes):
    answer = 0
    paths = []

    # 로봇별 이동 경로 구하기
    for route in routes:
        c_p = route[0]-1
        c_r, c_c = points[c_p][0]-1, points[c_p][1]-1
        path = [(c_r, c_c)]
        for n_p in route[1:]:
            n_p = n_p-1
            n_r, n_c = points[n_p][0]-1, points[n_p][1]-1
            
            # r 좌표가 변하는 이동을 c 좌표가 변하는 이동보다 먼저
            while n_r != c_r:
                if c_r > n_r:
                    c_r -= 1
                else:
                    c_r += 1
                path.append((c_r, c_c))
                
            while n_c != c_c:
                if c_c > n_c:
                    c_c -= 1
                else:
                    c_c += 1
                path.append((c_r, c_c))
        paths.append(path)


    # 충돌 지점 찾기
    longest_t = 0
    for path in paths:
        longest_t = max(longest_t, len(path))
        
    for t in range(longest_t):
        pos = defaultdict(int)
        
        for path in paths:
            if len(path) > t:
                pos[path[t]] += 1
                
        for p, cnt in pos.items():
            if cnt >= 2:
                answer += 1
                    
    return answer