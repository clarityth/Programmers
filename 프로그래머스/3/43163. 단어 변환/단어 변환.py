from collections import deque
def solution(begin, target, words):
    answer = 0
    def can_change(a, b) :
        diff = 0
        for i in range(len(a)) :
            if a[i] != b[i] :
                diff += 1
        return diff == 1
    
    q = deque([(begin, 0)])
    visited_set = set(begin)
    
    while q :
        word, cnt = q.popleft()
        
        if word == target :
            return cnt
            
        for next_word in words :
            if next_word not in visited_set and can_change(word, next_word):
                q.append((next_word, cnt+1))
                visited_set.add(next_word)
    
    return 0