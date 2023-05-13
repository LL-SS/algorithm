def solution(emergency):
    priority = {}
    answer = []
    
    emergency_sorted = sorted(emergency, reverse=True)
    
    for (i, v) in enumerate(emergency_sorted):
        priority[v] = i + 1
        
    for num in emergency:
        answer.append(priority[num])
    
    return answer