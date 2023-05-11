def solution(rsp):
    answer = ''
    
    counter = ['5', '0', '0', '0', '0', '2']
    
    for char in rsp:
        answer += counter[int(char)]
    
    return answer