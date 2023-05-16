def solution(my_str, n):
    answer = []
    string = ''
    
    for char in my_str:
        string += char
        
        if len(string) == n:
            answer.append(string)
            string = ''
            
    if len(string) > 0:
        answer.append(string)
        
    return answer