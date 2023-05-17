def solution(common):
    diff = common[1] - common[0]
    
    if 0 in common or common[2] - common[1] == diff:
        return common[-1] + diff
    
    else:
        return common[-1] * (common[1] / common[0])