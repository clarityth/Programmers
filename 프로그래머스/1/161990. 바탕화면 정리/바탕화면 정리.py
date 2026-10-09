def solution(wallpaper):
    lx = 50
    ly = 50
    rx = 0
    ry = 0
    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[0])) :
            if wallpaper[i][j] == '#' :
                lx = min(lx, j)
                ly = min(ly, i)
                rx = max(rx, j)
                ry = max(ry, i)
    answer = [ly, lx, ry + 1, rx + 1]
    return answer