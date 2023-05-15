def solution(bin1, bin2):
    num1 = int('0b' + bin1, 2)
    num2 = int('0b' + bin2, 2)
    
    answer = format(num1 + num2, 'b')
    
    return answer