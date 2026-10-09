from math import ceil
def solution(progresses, speeds):
    completed_time = []
    for p, s in zip(progresses, speeds) :
        completed_time.append(ceil((100-p)/s))
    
    answer = []
    basis_time = completed_time[0]
    count = 1
    
    for i in range(1, len(completed_time)) :
        if basis_time >= completed_time[i] :
            count += 1
        else :
            answer.append(count)
            basis_time = completed_time[i]
            count = 1
    answer.append(count)
    return answer