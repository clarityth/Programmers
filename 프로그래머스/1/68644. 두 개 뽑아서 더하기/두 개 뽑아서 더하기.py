def solution(numbers):
    num_set = set()
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)) :
            num_set.add(numbers[i]+numbers[j])
    answer = sorted(list(num_set))
    return answer