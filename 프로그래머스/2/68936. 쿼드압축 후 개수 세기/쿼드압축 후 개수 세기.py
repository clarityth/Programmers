def solution(arr):
    def quad_tree(x, y, size) :
        color = arr[y][x]
        for i in range(y, y+size) :
            for j in range(x, x+size) :
                if color != arr[i][j] :
                    half = size // 2
                    top_left = quad_tree(x, y, half)
                    top_right = quad_tree(x+half, y, half)
                    bottom_left = quad_tree(x, y+half, half)
                    bottom_right = quad_tree(x+half, y+half, half)
                    
                    return f"{top_left}{top_right}{bottom_left}{bottom_right}"
        return str(color)
    
    pressed_str = quad_tree(0, 0, len(arr))
    answer = [pressed_str.count('0'), pressed_str.count('1')]
    
    return answer