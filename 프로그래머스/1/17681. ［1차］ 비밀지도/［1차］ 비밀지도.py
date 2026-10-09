def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        # or 연산 결과를 2진수로 변환하고, "0b"을 지운뒤 길이가 n이 되도록 0을 문자열의 앞자리에 채워넣은 후 각 자리수를 리스트로 변환 
        or_result = list(map(int, bin(arr1[i] | arr2[i])[2:].zfill(n))) 
        ans = []
        for j in range(len(or_result)) :
            if or_result[j] == 1 : # 둘 중에 하나라도 벽이면 전체에서도 벽임
                ans.append('#')
            else :
                ans.append(' ')
        answer.append(''.join(ans))
    return answer