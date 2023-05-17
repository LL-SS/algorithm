def solution(numlist, n):
    diff = [(num, abs(num - n)) for num in numlist]
    
    diff.sort(key = lambda x: (x[1], -x[0]))
    
    return [num[0] for num in diff]