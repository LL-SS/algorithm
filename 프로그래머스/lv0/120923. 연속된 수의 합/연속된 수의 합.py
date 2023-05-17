def solution(num, total):
    answer = []
    
    mid = total // num
    scope = num // 2
    
    if num % 2 == 0:
        for i in range(mid - scope + 1, mid + scope + 1):
            answer.append(i)
        
    else:
        for i in range(mid - scope, mid + scope + 1):
            answer.append(i)
    
    return answer