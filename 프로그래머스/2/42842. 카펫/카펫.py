def solution(brown, yellow):
    for row in range(3, int((brown+yellow)**0.5)+1) :
        if (brown+yellow) % row == 0 :
            col = (brown+yellow) // row
            if brown == 2*row + 2*col-4 and yellow == (row-2)*(col-2) :
                return [col, row]
            
    return [-1]