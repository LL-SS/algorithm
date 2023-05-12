def solution(num, k):
    str_num = str(num)
    
    answer = str_num.find(str(k))
    
    if answer >= 0:
        return answer + 1
    
    return answer