def solution(score):
    score = list(map(lambda x: x[0] + x[1], score))
    
    order = {}
    
    for (i, v) in enumerate(sorted(score, reverse=True)):
        if v not in order:
            order[v] = i + 1
            
    answer = [order[i] for i in score]
        
    return answer