def solution(user_id, banned_id):
    def match_pattern(u, b) :
        if len(u) != len(b) :
            return False
        for i in range(len(u)) :
            if b[i] != '*' and b[i] != u[i] :
                return False
        return True
    
    candidates = []
    for b in banned_id :
        cand = []
        for u in user_id :
            if (match_pattern(u, b)) :
                cand.append(u)
        candidates.append(cand)
    
    # print(candidates)
    
    result = set()
    def dfs(idx, used) :
        if idx == len(banned_id) :
            result.add(frozenset(used))
            return
        for user in candidates[idx] :
            if user not in used :
                used.add(user)
                dfs(idx+1, used)
                used.remove(user)
    
    dfs(0, set())
    # print(result)
    return len(result)