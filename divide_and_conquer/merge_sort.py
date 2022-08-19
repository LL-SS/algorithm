def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    sorted_list = []

    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list1[0]:
            sorted_list.append(list1[0])
            del list1[0]

        elif list2[0] < list1[0]:
            sorted_list.append(list2[0])
            del list2[0]

        else:
            sorted_list.append(list1[0])
            del list1[0]

    if len(list1) == 0:
        return sorted_list + list2

    if len(list2) == 0:
        return sorted_list + list1

    return sorted_list

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) <= 1:
        return my_list

    else:
        mid = len(my_list) // 2
        return merge(merge_sort(my_list[:mid]), merge_sort(my_list[mid:]))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
