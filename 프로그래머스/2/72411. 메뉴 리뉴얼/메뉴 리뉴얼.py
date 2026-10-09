from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course :
        menu = []
        for order in orders :
            comb = combinations(sorted(order), c)
            menu.extend(comb)
            
        counter = Counter(menu)
        if counter :
            max_cnt = max(counter.values())

            if max_cnt >= 2 :
                for m, count in counter.items() :
                    if count == max_cnt : 
                        answer.append("".join(m))
    return sorted(answer)