from collections import defaultdict, Counter
def check(want, count) :
    for k, v in want.items() :
        if count[k] < v :
            return False
    return True

def solution(want, number, discount):
    answer = 0
    want_dict = defaultdict(int, zip(want, number))
    
    # 초기 10일 슬라이딩 윈도우 설정
    prefix_count = Counter(discount[:10])
    # 초기 윈도우 검사
    if check(want_dict, prefix_count) :
        answer += 1
    
    # 11일부터 슬라이딩 윈도우 이동, 검사
    for i in range(10, len(discount)) :
        prefix_count[discount[i-10]] -= 1
        prefix_count[discount[i]] += 1

        if check(want_dict, prefix_count) :
            answer += 1

    return answer