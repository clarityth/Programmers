def solution(files):
    answer = []
    preprocessed = []
    for i, file in enumerate(files):
        is_head = True
        is_number = False
        head = ''
        number = ''
        tail = ''
        for c in file:
            if is_head:
                if not c.isdigit():
                    head += c.lower()
                    
                else:
                    number += c
                    is_head = False
                    is_number = True
                    continue
                    
            elif is_number and len(number) < 5:
                if c.isdigit():
                    number += c
                else:
                    tail += c
                    is_number = False
                        
            else:
                tail += c
        preprocessed.append((i, head, int(number), tail))
        
    s_preprocessed = sorted(preprocessed, key=lambda x:(x[1], x[2], x[0]))
    
    for i, _, _, _ in s_preprocessed:
        answer.append(files[i])
        
    return answer