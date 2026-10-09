from collections import deque
def solution(maps):
    s = (0, 0)
    e = (0, 0)
    for i, m in enumerate(maps) :
        for j, c in enumerate(m) :
            if c == 'S' :
                s = (i, j)
            elif c == "E" :
                e = (i, j)
                
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    def bfs(maps, start, dest) :
        n = len(maps[0])
        m = len(maps)
        visited = [[[False] * 2 for _ in range(n)] for _ in range(m)]
        q = deque([(start, 0, 0)])
        visited[start[0]][start[1]][0] = True
        
        while q :
            cur, pressed, time = q.popleft()
            cur_y, cur_x = cur
            
            if (cur_y, cur_x) == dest and pressed == True :
                return time
                
            for i in range(4) :
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                
                if 0 <= next_x < n and 0 <= next_y < m and maps[next_y][next_x] != 'X' :
                    next_pressed = pressed if maps[next_y][next_x] != 'L' else 1

                    if not visited[next_y][next_x][next_pressed] :
                        visited[next_y][next_x][next_pressed] = True
                        q.append(((next_y, next_x), next_pressed, time + 1))
        return -1
    
    return bfs(maps, s, e)