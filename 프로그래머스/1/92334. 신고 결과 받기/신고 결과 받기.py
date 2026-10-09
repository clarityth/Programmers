from collections import defaultdict
def solution(id_list, report, k):
    report_dict = defaultdict(set)
    idx_dict = {}
    
    for i, name in enumerate(id_list) :
        idx_dict[name] = i
        
    for r in report :
        reporter, reported = r.split()
        report_dict[reported].add(reporter)
        
    answer = [0] * len(id_list)
    for _, data in report_dict.items() :
        if len(data) >= k :
            for reporter in data :
                answer[idx_dict[reporter]] += 1

    return answer