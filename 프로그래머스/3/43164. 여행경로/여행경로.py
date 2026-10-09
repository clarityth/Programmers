from collections import defaultdict
def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for a, b in tickets :
        routes[a].append(b)

    for data in routes.values() :
        data.sort(reverse=True)
    
    def dfs(depart) :
        nonlocal answer
        
        while routes[depart] :
            dfs(routes[depart].pop())
        answer.append(depart)
    
    dfs('ICN')
    return answer[::-1]