from collections import deque, defaultdict
def solution(record):
    answer = []
    nickname_dict = {}
    q = deque()
    
    for r in record :
        splitted_r = r.split()
        op = splitted_r[0]
        uid = splitted_r[1]
            
        if len(splitted_r) == 3 : # Enter or Change
            nickname = splitted_r[2]
            nickname_dict[uid] = nickname
        
        if op == "Enter" or op == "Leave" :
            q.append((op, uid))
    
    while q :
        op, uid = q.popleft()
        if op == "Enter" :
            answer.append(f"{nickname_dict[uid]}님이 들어왔습니다.")
        elif op == "Leave" :
            answer.append(f"{nickname_dict[uid]}님이 나갔습니다.")

    return answer