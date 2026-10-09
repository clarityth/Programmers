import heapq
def solution(n, works):
    answer = 0
    max_heap = [-x for x in works]
    heapq.heapify(max_heap)
    while n > 0 and max_heap:
        num = heapq.heappop(max_heap) + 1
        if num < 0 :
            heapq.heappush(max_heap, num)
        n -= 1
        
    return sum(x * x for x in max_heap)