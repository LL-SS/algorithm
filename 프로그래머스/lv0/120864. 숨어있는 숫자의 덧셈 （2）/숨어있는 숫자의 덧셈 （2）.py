def solution(my_string):
    answer = 0
    
    numbers = ''
    
    for char in my_string:
        if char.isdigit():
            numbers += char
        else:
            numbers += ' '
            
    numbers_list = numbers.split(' ')
    
    for num in numbers_list:
        if num.isdigit():
            answer += int(num)
    
    return answer