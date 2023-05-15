def solution(s):
    answer = []
    
    string = set(s)
    
    for char in string:
        if s.count(char) == 1:
            answer.append(char)
            
    answer = ''.join(sorted(answer))
            
    return answer