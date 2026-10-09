import re
def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    answer = re.sub(r'\.{2,}', '.', answer)
    answer = answer.strip('.')
    if answer == "" :
        answer = "a"
    answer = answer[:15].rstrip('.')
    while len(answer) < 3 :
        answer += answer[-1]
    return answer