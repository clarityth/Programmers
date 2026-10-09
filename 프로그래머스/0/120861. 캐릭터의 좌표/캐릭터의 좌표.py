def solution(keyinput, board):
    answer = []
    x = y = 0
    x_bound = [-1*(board[0]//2), board[0]//2]
    y_bound = [-1*(board[1]//2), board[1]//2]
    
    cmd = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    for key in keyinput :
        dx, dy = cmd[key]
        next_x = x+dx
        next_y = y+dy
        
        if x_bound[0] <= next_x <= x_bound[1] and y_bound[0] <= next_y <= y_bound[1] :
            x = next_x
            y = next_y

    return [x, y]