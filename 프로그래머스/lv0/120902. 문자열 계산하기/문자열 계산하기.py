def solution(my_string):
    string = my_string.split(' ')
    answer = int(string[0])
    
    for i in range(1, len(string), 2):
        if string[i] == '+':
            answer += int(string[i + 1])
        else:
            answer -= int(string[i + 1])
    
    return answer