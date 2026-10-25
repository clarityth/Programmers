def solution(book_time):
    answer = 1
    
    # 시간을 분 단위로 변환
    books = []
    for s, e in book_time:
        s_h, s_m = s.split(':')
        s_h, s_m = int(s_h), int(s_m)
        e_h, e_m = e.split(':')
        e_h, e_m = int(e_h), int(e_m)
        books.append([(s_h*60+s_m), (e_h*60+e_m+10)]) # 종료 시간에 청소 시간 포함
    
    # 종료 시간 기준으로 내림차순 정렬
    s_books = sorted(books, key=lambda x:(-x[1], -x[0]))
    rooms = [s_books[0][0]] # 각 방의 시작 시간을 저장, 기본 1개의 방으로 시작
    
    for s_m, e_m in s_books[1:]:
        avail = False # 기존 방에 들어갈 수 있는지
        # 들어갈 수 있는 방 탐색
        for i in range(len(rooms)):
            if rooms[i] >= e_m:
                rooms[i] = s_m
                avail = True
                break
        # 들어갈 수 있는 방이 없다면 새로운 방 배정
        if not avail:
            rooms.append(s_m)
            answer += 1
            
    return answer