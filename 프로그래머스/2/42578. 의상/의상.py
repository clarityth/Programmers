from collections import defaultdict
def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)
    for (cloth, category) in clothes :
        clothes_dict[category] += 1
        
    for (category, cnt) in clothes_dict.items() :
        answer *= (cnt + 1)
        
    return answer - 1