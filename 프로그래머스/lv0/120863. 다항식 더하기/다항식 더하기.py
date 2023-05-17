def solution(polynomial):
    polynomial_list = polynomial.split(' + ')
    
    c = 0
    x = 0
    
    for num in polynomial_list:
        if num.isdigit():
            c += int(num)
        else:
            if num[:-1]:
                x += int(num[:-1])
            else:
                x += 1
                
    if x > 1:
        x = str(x) + 'x'
    elif x == 1:
        x = 'x'
    else:
        x = ''
        
    if c > 0:
        c = str(c)
    else:
        c = ''
        
    if x and c:
        return x + ' + ' + c
    elif x:
        return x
    else:
        return c