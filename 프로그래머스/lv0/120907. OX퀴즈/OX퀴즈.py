def solution(quiz):
    answer = []
    
    for question in quiz:
        if eval(question.split(' = ')[0]) == int(question.split(' = ')[1]):
            answer.append('O')
        else:
            answer.append('X')

    return answer