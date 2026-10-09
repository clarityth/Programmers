def solution(s):
    answer = []
    split_s = s[2:-2].split('},{')
    split_s.sort(key=len)
    
    seen = set()
    for num_str in split_s :
        nums = num_str.split(',')
        for num in nums :
            if num not in seen :
                seen.add(num)
                answer.append(int(num))

    return answer