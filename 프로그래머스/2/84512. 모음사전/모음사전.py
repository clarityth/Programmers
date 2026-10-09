def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    def dfs(cur_word) :
        if len(cur_word) == 5 :
            return
        
        for i in range(5) :
            dictionary.append(cur_word+vowels[i])
            dfs(cur_word+vowels[i])
                
    dfs("")

    return dictionary.index(word)+1