def solution(s):
    answer = ''
    words = s.split(' ')
    print(words)
    for i, word in enumerate(words) :
        if word :
            answer += word[0].upper() + word[1:].lower()
        else :
            answer += ''
            
        if i < len(words) - 1 :
            answer += ' '

    return answer