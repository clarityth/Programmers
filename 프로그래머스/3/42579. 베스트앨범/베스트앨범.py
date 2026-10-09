from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(lambda: {'songs': [], 'total': 0 }) # 중첩 딕셔너리
    for idx, (genre, play) in enumerate(zip(genres, plays)) :
        genre_dict[genre]['songs'].append((idx, play))
        genre_dict[genre]['total'] += play
        
    # print(genre_dict.items())
    sorted_genre = sorted(genre_dict.items(), key = lambda x: -x[1]['total']) # items()로 리스트 변환 -> 중첩 딕셔너리 내부의 'total' 키를 기준으로 내림차순 정렬
    
    for genre, data in sorted_genre :
        # print(data)
        sorted_songs = sorted(data['songs'], key = lambda x: -x[1]) # 중첩 딕셔너리의 'songs' 키의 내부 튜플 중 2번째 원소(play)를 기준으로 내림차순 정렬
        # print(sorted_songs)
        for idx, _ in sorted_songs[:2] : # 장르별 상위 2개까지 정답에 인덱스 삽입
            answer.append(idx)
    
    return answer