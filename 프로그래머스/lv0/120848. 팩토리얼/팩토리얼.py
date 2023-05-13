def solution(n):
    i = 1
    j = 0
    
    while i <= n:
        j += 1
        i *= j
    
    return j - 1