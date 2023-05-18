def solution(board):
    answer = 0
    
    n = len(board)
    
    if n == 1:
        return board[0].count(0)
    
    result = [[0 for i in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == 0:
                if j == 0:
                    if [board[i][j], board[i][j + 1], board[i + 1][j], board[i + 1][j + 1]].count(1) > 0:
                        result[i][j] = 1
                elif j == n - 1:
                    if [board[i][j - 1], board[i][j], board[i + 1][j - 1], board[i + 1][j]].count(1) > 0:
                        result[i][j] = 1
                else:
                    if [board[i][j - 1], board[i][j], board[i][j + 1], board[i + 1][j - 1], board[i + 1][j], board[i + 1][j + 1]].count(1) > 0:
                        result[i][j] = 1
                        
            elif i == n - 1:
                if j == 0:
                    if [board[i - 1][j], board[i - 1][j + 1], board[i][j], board[i][j + 1]].count(1) > 0:
                        result[i][j] = 1
                elif j == n - 1:
                    if [board[i - 1][j - 1], board[i - 1][j], board[i][j - 1], board[i][j]].count(1) > 0:
                        result[i][j] = 1
                else:
                    if [board[i - 1][j - 1], board[i - 1][j], board[i - 1][j + 1], board[i][j - 1], board[i][j], board[i][j + 1]].count(1) > 0:
                        result[i][j] = 1
            
            else:
                if j == 0:
                    if [board[i - 1][j], board[i - 1][j + 1], board[i][j], board[i][j + 1], board[i + 1][j], board[i + 1][j + 1]].count(1) > 0:
                        result[i][j] = 1
                elif j == n - 1:
                    if [board[i - 1][j - 1], board[i - 1][j], board[i][j - 1], board[i][j], board[i + 1][j -1], board[i + 1][j]].count(1) > 0:
                        result[i][j] = 1
                else:
                    if [board[i - 1][j - 1], board[i - 1][j], board[i - 1][j + 1], board[i][j - 1], board[i][j], board[i][j + 1], board[i + 1][j - 1], board[i + 1][j], board[i + 1][j + 1]].count(1) > 0:
                        result[i][j] = 1
                        
    for num in result:
        answer += num.count(0)
                
    return answer