# floyd-warshall
def solution(n, results):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)] # 0: 모름, -1: 짐, 1: 이김
    for w, l in results : # 확정된 결과를 기록
        graph[w][l] = 1
        graph[l][w] = -1
    
    for k in range(1, n+1) :
        for i in range(1, n+1) :
            for j in range(1, n+1) :
                if graph[i][k] == 1 and graph[k][j] == 1 : # i가 k에게 이겼는데 k가 j를 이겼다면, i가 j를 이김
                    graph[i][j] = 1 # i가 j를 이김
                    graph[j][i] = -1 # j가 i한테 짐
                    
    for i in range(1, n+1) : # 모든 선수들에 대해 순회
        known = 0 # 알고 있는 결과를 누적
        for j in range(1, n+1) :
            if i == j :
                continue
                
            if graph[i][j] != 0 : # 모르는 결과 제외
                known += 1 
                
        if known == n-1 : # 자신을 제외하고 모든 결과를 알고있다면
            answer += 1 # 정답 증가
            
    return answer