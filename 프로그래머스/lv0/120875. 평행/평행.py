def solution(dots):
    answer = 0

    idx_1 = [(0, 1), (0, 2), (0, 3)]
    idx_2 = [(2, 3), (1, 3), (1, 2)]

    for i in range(3):
        x1, y1, x2, y2 = dots[idx_1[i][0]][0], dots[idx_1[i][0]][1], dots[idx_1[i][1]][0], dots[idx_1[i][1]][1]
        x3, y3, x4, y4 = dots[idx_2[i][0]][0], dots[idx_2[i][0]][1], dots[idx_2[i][1]][0], dots[idx_2[i][1]][1]

        if abs(y2 - y1) / abs(x2 - x1) == abs(y4 - y3) / abs(x4 - x3):
            answer = 1

    return answer