def solution(n):
    answer = 0
    
    if n <= 3:
        answer = 0
        
    for i in range(4, n + 1):
        div = 0
        
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        
        if div >= 3:
            answer += 1
    
    return answer