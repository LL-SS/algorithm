def solution(spell, dic):
    word = sorted(''.join(spell))
    
    for dic_word in dic:
        if word == sorted(dic_word):
            return 1
    
    return 2