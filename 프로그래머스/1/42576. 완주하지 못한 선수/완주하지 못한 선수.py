def solution(participant, completion):
    hash_dict = {}
    hash_sum = 0
    
    for p in participant :
        hash_sum += hash(p)
        hash_dict[hash(p)] = p
    
    for c in completion :
        hash_sum -= hash(c)
    
    return hash_dict[hash_sum]