def solution(array, n):
    diff = []
    
    for num in array:
        diff.append(abs(num - n))
        
    if n - min(diff) in array:
        answer = n - min(diff)
    else:
        answer = n + min(diff)
    
    return answer