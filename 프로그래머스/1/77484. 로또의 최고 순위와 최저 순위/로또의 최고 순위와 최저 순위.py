def solution(lottos, win_nums):
    wins = set(win_nums)
    match_rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    zero_cnt = lottos.count(0)
    correct_cnt = 0
    for num in lottos :
        if num in wins :
            correct_cnt += 1
    answer = [match_rank[correct_cnt + zero_cnt], match_rank[correct_cnt]]
    return answer