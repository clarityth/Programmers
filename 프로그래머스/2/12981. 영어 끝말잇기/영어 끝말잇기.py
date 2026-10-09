def solution(n, words):
    word_set = set()
    prev_last = words[0][0]
    
    for i, word in enumerate(words) :
        if word[0] != prev_last or word in word_set or len(word) == 1 :
            return [(i % n) + 1, (i // n) + 1]
        
        word_set.add(word)
        prev_last = word[-1]
    return [0, 0]