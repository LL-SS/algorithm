def solution(cipher, code):
    answer = ''
    
#     iter = code - 1
    
#     while iter < len(cipher):
#         answer += cipher[iter]
#         iter += code
    
    for i in range(1, (len(cipher) // code) + 1):
        answer += cipher[(i * code) - 1]
    
    return answer