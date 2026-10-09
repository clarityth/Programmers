def solution(number, limit, power):
    answer = 0
    cnts = [0] * (number + 1)
    # 1 ~ number까지 해당되는 수들의 모든 약수의 개수를 한번에 구함 (에라토스테네스의 체 응용)
    for i in range(1, number + 1) :
        for j in range(i, number + 1, i) :
            cnts[j] += 1
    for i in range(1, number + 1) :
        if cnts[i] > limit :
            answer += power
        else :
            answer += cnts[i]
    return answer