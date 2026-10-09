def solution(board, h, w):
    answer = 0
    n = len(board)
    target = board[h][w]
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    for i in range(4) :
        nexth = h + dh[i]
        nextw = w + dw[i]
        if 0 <= nexth < n and 0 <=nextw < n and board[nexth][nextw] == target :
            answer += 1
    return answer