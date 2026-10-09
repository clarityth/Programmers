def solution(n):
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    
    triangle = [[0]*i for i in range(1, n+1)]
    
    dirs = 0
    cur_x, cur_y = 0, 0
    for num in range(1, n*(n+1)//2 +1) :
        triangle[cur_y][cur_x] = num
        next_x, next_y = cur_x+dx[dirs], cur_y+dy[dirs]
        
        if next_y >= n or next_x > next_y or triangle[next_y][next_x] != 0:
            dirs = (dirs + 1) % 3
            next_x, next_y = cur_x+dx[dirs], cur_y+dy[dirs]
        cur_x, cur_y = next_x, next_y

    answer = sum(triangle, [])
    return answer