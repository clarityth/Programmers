def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    def linear(arr) :
        prev2, prev1 = 0, 0
        for i in range(len(arr)) :
            prev2, prev1 = prev1, max(prev1, prev2 + arr[i])
        return prev1
        
    return max(linear(sticker[1:]), linear(sticker[:-1]))
    