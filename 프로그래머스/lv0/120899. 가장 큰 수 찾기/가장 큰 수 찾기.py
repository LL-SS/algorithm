def solution(array):
    for (i, v) in enumerate(array):
        if i == 0:
            max_value = v
            max_index = i
        else:
            if v > max_value:
                max_value = v
                max_index = i
                
    return [max_value, max_index]