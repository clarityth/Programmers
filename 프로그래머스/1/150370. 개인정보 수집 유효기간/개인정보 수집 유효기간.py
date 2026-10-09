from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    y, m, d = map(int, today.split('.'))
    total_d = y*12*28 + m*28 + d
    
    term_dict = {}
    for term in terms:
        name, expire_month = term.split()
        term_dict[name] = int(expire_month)*28
    
    # print(term_dict)
    
    for i, record in enumerate(privacies) :
        record_date, term = record.split()
        record_y, record_m, record_d = map(int, record_date.split('.'))
        record_total_d = record_y*12*28 + record_m*28 + record_d
        # print(total_d, record_total_d + term_dict[term])
        if total_d >= record_total_d + term_dict[term] :
            answer.append(i+1)

    return answer