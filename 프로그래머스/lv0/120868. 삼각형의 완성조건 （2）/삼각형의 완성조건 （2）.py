def solution(sides):
    answer = []
    
    for i in range(1, max(sides) + 1):
        if i + min(sides) > max(sides):
            answer.append(i)
    
    for i in range(max(sides) + 1, sum(sides)):
        answer.append(i)
    
    return len(answer)