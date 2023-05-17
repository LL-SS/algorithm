def solution(a, b):
    gcd = get_gcd(a, b)
    
    b /= gcd
    
    while b % 2 == 0:
        b /= 2
        
    while b % 5 == 0:
        b /= 5
        
    if b == 1:
        return 1
    else:
        return 2

def get_gcd(a, b):
    while b > 0:
        temp = a % b
        a = b
        b = temp
    
    return a