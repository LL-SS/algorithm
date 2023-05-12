def solution(age):
    answer = ''
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    while age > 0:
        answer += chars[age % 10]
        age = age // 10
    
    return answer[::-1]