def solution(n, w, num):
    answer = 1
    stack = []
    for i in range(n) :
        height = i // w
        col = 0
        if height % 2 == 0 : # 짝수 층의 경우 왼->오
            col = i % w
        else :
            col =  w - 1 - (i % w) # 홀수 층의 경우 오->왼
        if i + 1 == num :
            target_height = height
            target_col = col
        stack.append((height, col))
        
    for h, c in reversed(stack) :
        if h > target_height and c == target_col :
            answer += 1
        if h == target_height :
            break
            
    return answer