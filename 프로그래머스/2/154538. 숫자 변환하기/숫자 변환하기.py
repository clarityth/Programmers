from collections import deque
def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    
    cnts = [1000001] * (y+1)
    cnts[x] = 0
    
    while q :
        nowx, nowcnt = q.popleft()
        next_xs = [nowx*3, nowx*2, nowx+n]
        next_cnt = nowcnt+1
        for i in range(3) :
            if next_xs[i] <= y and cnts[next_xs[i]] > next_cnt :
                q.append((next_xs[i], next_cnt))
                cnts[next_xs[i]] = next_cnt
    
    return cnts[y] if cnts[y] != 1000001 else -1