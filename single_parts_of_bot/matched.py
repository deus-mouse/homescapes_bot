matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 4, 1, 3, 3, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 5, 1, 5, 1, 4, 3, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 5, 4, 2, 5, 4, 3, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 3, 2, 3, 1, 5, 5, 1, 3, 0, 0, 0, 0],
          [0, 0, 0, 0, 5, 3, 3, 0, 0, 3, 3, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 2, 4, 4, 3, 2, 4, 1, 2, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 1, 3, 5, 3, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 3, 3, 2, 4, 3, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

bonus_value = 9
primary = [2, 3]

def reverse_matrix(matrix):
    rev_matrix = []
    for n, i in enumerate(matrix[0]):  # assuming the lists are in the same length
        templist = []
        for l in matrix:
            templist.append(l[n])
        rev_matrix.append(templist)
    return rev_matrix


def matched(matrix, primary):
    # Ищем совпадения по горизонтали, получаем списки с индексами второго из совпавших
    # В развернутой матрице нижнего из совпавших (по вертикали)
    matched_list_in_line = []
    matched_list_in_column = []
    priority_list_in_line = []
    priority_list_in_column = []
    bonus_list = []

    for line in range(len(matrix)):
        matrix_line = matrix[line]
        # CODE REVIEW
        # for line in matrix:

        # сначала ищем в строках бонусы. будем лопать их первыми
        if bonus_value in matrix_line:
            list = []
            index = matrix_line.index(bonus_value)
            list.append(line)
            list.append(index)
            bonus_list.append(list)
            # CODE REVIEW
            # bonus_list.append([line, index])

            # по логике мы можем сразу совершить действие.
            # return play_actions(bonus_list)

        # получаем список где первое значение это индекс значения в линии, второе значение это его код/hook
        matched_in_line = [index for (index, value)
                   in enumerate(matrix[line])  # enumerate отдает (index в текущей строке, его значение), мы берем index
                   if value == matrix[line][index - 1] and matrix[line][index] != 0]
        if matched_in_line:
            for index in matched_in_line:
                list = []
                value = matrix[line][index]
                list.append(line)
                list.append(index)
                # если значение из списка целей
                if value in primary:
                    priority_list_in_line.append(list)
                    # CODE REVIEW
                    # priority_list_in_line.append([line, index])

                else:
                    matched_list_in_line.append(list)
                    # CODE REVIEW
                    # matched_list_in_line.append([line, index])

    # Чтобы найти пары по вертикали нужно развернуть матрицу.
    rev_matrix = reverse_matrix(matrix)
    for line in rev_matrix:
        print(line)
    for line in range(len(rev_matrix)):
        matrix_line = rev_matrix[line]
        # CODE REVIEW
        # for line in matrix:

        # получаем список где первое значение это индекс значения в линии, второе значение это его код/hook
        matched_in_line = [index for (index, value)
                   in enumerate(rev_matrix[line])  # enumerate отдает (index в текущей строке, его значение), мы берем index
                   if value == rev_matrix[line][index - 1] and rev_matrix[line][index] != 0]
        if matched_in_line:
            for index in matched_in_line:
                list = []
                value = rev_matrix[line][index]
                # т.к. матрица развернута, то и значения в списке нужно поменять местами.
                # было [line, index] / стало [index, line]
                list.append(index)
                list.append(line)
                # если значение из списка целей
                if value in primary:
                    priority_list_in_column.append(list)
                    # CODE REVIEW
                    # priority_list_in_line.append([index, line])

                else:
                    matched_list_in_column.append(list)
                    # CODE REVIEW
                    # matched_list_in_line.append([index, line])

    return priority_list_in_line, priority_list_in_column, matched_list_in_line, matched_list_in_column, bonus_list


matched = matched(matrix, primary)

priority_list_in_line = matched[0]
priority_list_in_column = matched[1]
matched_list_in_line = matched[2]
matched_list_in_column = matched[3]
bonus_list = matched[4]

print(f"{priority_list_in_line=}")
print(f"{priority_list_in_column=}")
print(f"{matched_list_in_line=}")
print(f"{matched_list_in_column=}")
print(f"{bonus_list=}")
