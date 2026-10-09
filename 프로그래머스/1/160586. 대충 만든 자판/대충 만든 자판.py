from collections import defaultdict
def solution(keymap, targets):
    answer = []
    keydict = defaultdict(lambda: -1)
    for keys in keymap :
        for i, key in enumerate(keys) :
            if keydict[key] > i + 1 or keydict[key] == -1:
                keydict[key] = i + 1
    
    for target in targets :
        isPossible = True
        cnt = 0
        for key in target :
            if keydict[key] == -1 :
                answer.append(-1)
                isPossible = False
                break
            else :
                cnt += keydict[key]
        if isPossible :
            answer.append(cnt)
    return answer