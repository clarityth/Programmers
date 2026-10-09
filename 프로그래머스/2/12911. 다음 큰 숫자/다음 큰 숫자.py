def solution(n):
    n_bin = str(bin(n))[2:]
    n_one_cnt = n_bin.count('1')

    for i in range(n+1, 1000001) :
        i_bin = str(bin(i))[2:]
        i_one_cnt = i_bin.count('1')

        if n_one_cnt == i_one_cnt :
            return i
    return None