def solution(order):
    answer = 0
    
    while order > 0:
        if ((order % 10) % 3 == 0 and (order % 10) != 0):
            answer += 1        
        order = order // 10
    
    return answer