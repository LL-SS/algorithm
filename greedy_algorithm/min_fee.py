def min_fee(pages_to_print):
    # 코드를 작성하세요.
    total_fee = 0

    pages_to_print.sort()

    for i in range(len(pages_to_print)):
        total_fee += pages_to_print[i] * (len(pages_to_print) - i)

    return total_fee

# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))