def solution(dots):
    dots.sort(key = lambda x: (x[0], x[1]))
    
    width = dots[2][0] - dots[0][0]
    height = dots[1][1] - dots[0][1]
    
    return width * height