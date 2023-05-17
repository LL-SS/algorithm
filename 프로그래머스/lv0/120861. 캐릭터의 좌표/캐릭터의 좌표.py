def solution(keyinput, board):
    border = [board[0] // 2, board[1] // 2]
    answer = [0, 0]
    
    for key in keyinput:
        if key == 'left' and answer[0] - 1 >= -(border[0]) :
            answer[0] -= 1
        elif key == 'right' and answer[0] + 1 <= border[0]:
            answer[0] += 1
        elif key == 'up' and answer[1] + 1 <= border[1]:
            answer[1] += 1
        elif key == 'down' and answer[1] - 1 >= -(border[1]):
            answer[1] -= 1
        
    return answer