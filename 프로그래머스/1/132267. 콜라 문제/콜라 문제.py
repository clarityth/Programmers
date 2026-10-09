def solution(a, b, n):
    answer = 0
    while n >= a :
        bonus = (n // a) * b
        n %= a
        n += bonus
        answer += bonus
    return answer