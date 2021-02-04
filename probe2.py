
word = 'referee'

original_matrix = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 4, 1, 3, 3, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 5, 1, 5, 1, 4, 3, 0, 0, 0, 0],
                   [0, 0, 0, 0, 5, 4, 2, 5, 4, 3, 0, 0, 0, 0],
                   [0, 0, 0, 3, 2, 3, 1, 5, 5, 1, 3, 0, 0, 0],
                   [0, 0, 0, 5, 3, 3, 0, 0, 3, 3, 1, 0, 0, 0],
                   [0, 0, 0, 2, 4, 4, 3, 2, 4, 1, 2, 0, 0, 0],
                   [0, 0, 0, 0, 1, 1, 3, 5, 3, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 3, 3, 2, 4, 3, 2, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

original_matrix2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 4, 1, 3, 3, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 5, 1, 5, 1, 4, 3, 0, 0, 0, 0],
                   [0, 0, 0, 6, 5, 4, 6, 5, 4, 3, 0, 0, 0, 0],
                   [0, 0, 0, 6, 2, 5, 6, 5, 5, 1, 3, 0, 0, 0],
                   [0, 0, 6, 5, 6, 6, 0, 6, 1, 3, 1, 0, 0, 0],
                   [0, 0, 0, 6, 4, 4, 6, 2, 4, 1, 2, 0, 0, 0],
                   [0, 0, 0, 6, 1, 1, 6, 5, 3, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 3, 3, 2, 4, 3, 2, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



def reverse_matrix(matrix):
    reverse_matrix = []
    for n, i in enumerate(matrix[0]):  # assuming the lists are in the same length
        templist = []
        for l in matrix:
            templist.append(l[n])
        # print("templist: ", n, "content: ", templist)
        reverse_matrix.append(templist)
    # for column in newmatrix:
    #     print(column)
    return reverse_matrix

def find_five_mathes(matrix, line, index):
    # Ищем совпадение на 5
    value = matrix[line][index]
    try:
        if matrix[line - 1][index - 2] == value and matrix[line - 2][index - 2] == value:
            #  совпадение top left
            print('совпадение top left')
            print('original_matrix2[line-1][index-2]', matrix[line - 1][index - 2])
            print('original_matrix2[line-2][index-2]', matrix[line - 2][index - 2])

            #  ищем возможность сложить
            if matrix[line][index - 3] == value:
                # нашли. двигаем слева направо
                print('!!! нашли 5. двигаем слева направо')
                direction = 'to right'
                move_index = [line, index - 3]
                print('move_index', move_index)
            elif matrix[line + 1][index - 2] == value:
                # нашли. двигаем снизу наверх
                print('!!! нашли 5. двигаем снизу наверх')
                direction = 'to up'
                move_index = [line + 1, index - 2]
                print('move_index', move_index)
            else:
                print('не нашли возможность')

        elif matrix[line - 1][index + 1] == value and matrix[line - 2][index + 1] == value:
            #  совпадение top right
            print('совпадение top right')
            #  ищем возможность сложить
            if matrix[line][index + 2] == value:
                # нашли. двигаем справа налево
                print('!!! нашли 5. двигаем справа налево')
                direction = 'to left'
                move_index = [line, index + 2]
                print('move_index', move_index)
            elif matrix[line + 1][index + 1] == value:
                # нашли. двигаем снизу наверх
                print('!!! нашли 5. двигаем снизу наверх')
                direction = 'to up'
                move_index = [line + 1, index + 1]
                print('move_index', move_index)
            else:
                print('не нашли возможность')

        elif matrix[line + 1][index - 2] == value and matrix[line + 2][index - 2] == value:
            #  совпадение lower left
            print('совпадение lower left')
            #  ищем возможность сложить
            if matrix[line][index - 3] == value:
                # нашли. двигаем слева направо
                print('!!! нашли. двигаем слева направо')
                direction = 'to right'
                move_index = [line, index - 3]
                print('move_index', move_index)
            elif matrix[line - 1][index - 2] == value:
                # нашли. двигаем сверху вниз
                print('!!! нашли 5. двигаем сверху вниз')
                direction = 'to down'
                move_index = [line - 1, index - 2]
                print('move_index', move_index)
            else:
                print('не нашли возможность')

        elif matrix[line + 1][index + 1] == value and matrix[line + 2][index + 1] == value:
            #  совпадение lower right
            print('совпадение lower right')
            #  ищем возможность сложить
            if matrix[line][index + 2] == value:
                # нашли. двигаем справа налево
                print('!!! нашли 5. двигаем справа налево')
                direction = 'to left'
                move_index = [line, index + 2]
                print('move_index', move_index)
            elif matrix[line - 1][index + 1] == value:
                # нашли. двигаем сверху вниз
                print('!!! нашли 5. двигаем сверху вниз')
                direction = 'to down'
                move_index = [line - 1, index + 1]
                print('move_index', move_index)
            else:
                print('не нашли возможность')

        return move_index, direction

    except Exception as ex:
        print('except', ex)
        pass

def find_square_mathes(matrix, line, index):
    # Ищем совпадение на квадрат
    value = matrix[line][index]
    try:
        if matrix[line - 1][index - 1] == value:
            #  совпадение top left
            print('совпадение top left')
            # print('original_matrix2[line-1][index-2]', matrix[line - 1][index - 2])
            # print('original_matrix2[line-2][index-2]', matrix[line - 2][index - 2])
            #  ищем возможность сложить
            if matrix[line - 1][index + 1] == value:
                # нашли. двигаем справа налево
                print('!!! нашли 4. двигаем справа налево')
                direction = 'to left'
                move_index = [line - 1, index + 1]
                print('move_index', move_index)
            elif matrix[line - 2][index] == value:
                # нашли. двигаем сверху вниз
                print('!!! нашли 4. двигаем сверху вниз')
                direction = 'to down'
                move_index = [line - 2, index]
                print('move_index', move_index)
            else:
                print('не нашли возможность')

        elif matrix[line - 1][index] == value:
            #  совпадение top right
            print('совпадение top right')
            # print('original_matrix2[line-1][index-2]', matrix[line - 1][index - 2])
            # print('original_matrix2[line-2][index-2]', matrix[line - 2][index - 2])
            #  ищем возможность сложить
            if matrix[line - 1][index - 2] == value:
                # нашли. двигаем слева направо
                print('!!! нашли 4. двигаем слева направо')
                direction = 'to right'
                move_index = [line - 1, index - 2]
                print('move_index', move_index)
            elif matrix[line - 2][index - 1] == value:
                # нашли. двигаем сверху вниз
                print('!!! нашли 4. двигаем сверху вниз')
                direction = 'to down'
                move_index = [line - 2, index - 1]
                print('move_index', move_index)
            else:
                print('не нашли возможность')

        elif matrix[line + 1][index - 1] == value:
            #  совпадение lower left
            print('совпадение lower left')
            # print('original_matrix2[line-1][index-2]', matrix[line - 1][index - 2])
            # print('original_matrix2[line-2][index-2]', matrix[line - 2][index - 2])
            #  ищем возможность сложить
            if matrix[line + 1][index + 1] == value:
                # нашли. двигаем справа налево
                print('!!! нашли 4. двигаем справа налево')
                direction = 'to left'
                move_index = [line - 1, index - 2]
                print('move_index', move_index)
            elif matrix[line + 2][index] == value:
                # нашли. двигаем снизу вверх
                print('!!! нашли 4. двигаем снизу вверх')
                direction = 'to up'
                move_index = [line + 2, index]
                print('move_index', move_index)
            else:
                print('не нашли возможность')

        elif matrix[line + 1][index] == value:
            #  совпадение lower right
            print('совпадение lower right')
            # print('original_matrix2[line-1][index-2]', matrix[line - 1][index - 2])
            # print('original_matrix2[line-2][index-2]', matrix[line - 2][index - 2])
            #  ищем возможность сложить
            if matrix[line + 1][index - 2] == value:
                # нашли. двигаем справа налево
                print('!!! нашли 4. двигаем справа налево')
                direction = 'to left'
                move_index = [line - 1, index - 2]
                print('move_index', move_index)
            elif matrix[line + 2][index] == value:
                # нашли. двигаем снизу вверх
                print('!!! нашли 4. двигаем снизу вверх')
                direction = 'to up'
                move_index = [line + 2, index]
                print('move_index', move_index)
            else:
                print('не нашли возможность')

        return move_index, direction

    except Exception as ex:
        print('except', ex)
        pass

def find_three_mathes_in_line(matrix, line, index):
    value = matrix[line][index]
    try:
        # Ищем совпадение на тройку в ряд
        #  ищем возможность сложить
        if matrix[line - 1][index - 2] == value:
            #  совпадение top left
            print('совпадение top left')
            # нашли. двигаем сверху вниз
            print('!!! нашли 3g. двигаем сверху вниз')
            direction = 'to down'
            move_index = [line - 1, index - 2]
            print('move_index', move_index)

        elif matrix[line][index - 3] == value:
            #  совпадение middle left
            print('совпадение middle left')
            # нашли. двигаем слева направо
            print('!!! нашли 3g. двигаем слева направо')
            direction = 'to right'
            move_index = [line, index - 3]
            print('move_index', move_index)

        elif matrix[line + 1][index - 2] == value:
            #  совпадение lower left
            print('совпадение lower left')
            # нашли. двигаем снизу наверх
            print('!!! нашли 3g. двигаем снизу наверх')
            direction = 'to up'

            move_index = [line + 1, index - 2]
            print('move_index', move_index)

        elif matrix[line - 1][index + 1] == value:
            #  совпадение top right
            print('совпадение top right')
            # нашли. двигаем сверху вниз
            print('!!! нашли 3g. двигаем сверху вниз')
            direction = 'to down'
            move_index = [line - 1, index + 1]
            print('move_index', move_index)

        elif matrix[line][index + 2] == value:
            #  совпадение middle right
            print('совпадение middle right')
            # нашли. двигаем справа налево
            print('!!! нашли 3g. двигаем справа налево')
            direction = 'to left'
            move_index = [line, index + 2]
            print('move_index', move_index)

        elif matrix[line + 1][index + 1] == value:
            #  совпадение lower right
            print('совпадение lower right')
            # нашли. двигаем снизу вверх
            print('!!! нашли 3g. двигаем снизу вверх')
            direction = 'to up'
            move_index = [line + 1, index + 1]
            print('move_index', move_index)

        return move_index, direction

    except Exception as ex:
        print('except', ex)
        pass



def find_three_mathes_in_column(matrix):
    # value = matrix[line][index]
    # reverse_matrix = []
    # for n, i in enumerate(matrix[0]):  # assuming the lists are in the same length
    #     templist = []
    #     for l in matrix:
    #         templist.append(l[n])
    #     # print("templist: ", n, "content: ", templist)
    #     reverse_matrix.append(templist)
    # # for column in newmatrix:
    # #     print(column)
    # new_matched = matched(reverse_matrix)

    matrix = reverse_matrix(matrix)
    matched_list = matched(matrix)

    for index, line in matched_list:
        # print('matched', matched)
        # print('full index = ', line, index)
        value = matrix[line][index]
        # print('value', value)
        # print('value', value)
        try:
            # Ищем совпадение на тройку в столбец
            #  ищем возможность сложить
            if reverse_matrix[line - 1][index - 2] == value:
                #  совпадение top left
                print('совпадение top left', value)
                # нашли. двигаем слева направо
                print('!!! нашли. двигаем слева направо')
                move_index = [line - 1, index - 2]
                print('move_index', move_index)
                move_index.reverse()
                print('move_index_reverse', move_index)

            if reverse_matrix[line][index - 3] == value:
                #  совпадение top middle
                print('совпадение top middle', value)
                # нашли. двигаем сверху вниз
                print('!!! нашли. двигаем сверху вниз')
                move_index = [line, index - 3]
                print('move_index', move_index)
                move_index.reverse()
                print('move_index_reverse', move_index)

            if reverse_matrix[line + 1][index - 2] == value:
                #  совпадение top right
                print('совпадение top right', value)
                # нашли. двигаем справа налево
                print('!!! нашли. двигаем справа налево')
                move_index = [line + 1, index - 2]
                print('move_index', move_index)
                move_index.reverse()
                print('move_index_reverse', move_index)

            if reverse_matrix[line - 1][index + 1] == value:
                #  совпадение lower left
                print('совпадение lower left', value)
                # нашли. двигаем слева направо
                print('!!! нашли. двигаем слева направо')
                move_index = [line - 1, index + 1]
                print('move_index', move_index)
                move_index.reverse()
                print('move_index_reverse', move_index)

            if reverse_matrix[line][index + 2] == value:
                #  совпадение low middle
                print('совпадение low middle', value)
                # нашли. двигаем справа налево
                print('!!! нашли. двигаем снизу вверх')
                move_index = [line, index + 2]
                print('move_index', move_index)
                move_index.reverse()
                print('move_index_reverse', move_index)

            if reverse_matrix[line + 1][index + 1] == value:
                #  совпадение lower right
                print('совпадение lower right', value)
                # нашли. двигаем справа налево
                print('!!! нашли. двигаем справа налево')
                move_index = [line + 1, index + 1]
                print('move_index', move_index)
                move_index.reverse()
                print('move_index_reverse', move_index)

        except Exception as ex:
            print('except', ex)
            pass


# не доделано
def matched(matrix):
    # Ищем совпадения по горизонтали, получаем списки с индексами второго из совпавших
    matched_list = []
    for line in range(len(matrix)):
        # print([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
        #        and original_matrix[line][index] != 0])
        # matched_list.append([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
        #        and original_matrix[line][index] != 0])
        matched = [index for (index, letter) in enumerate(matrix[line])
                   if letter == matrix[line][index - 1] and matrix[line][index] != 0]
        # matched_list.append(matched)
        # print('matched', matched)
        if matched:
            print('matched', matched)
            for index in matched:
                list = []
                # print('matched', matched)
                print('full index = ', line, index)
                value = matrix[line][index]
                list.append(line)
                list.append(index)
                matched_list.append(list)
    return matched_list

matched = matched(original_matrix2)
print(matched)



# for line, index in matched:
#     # print(line, index)
#     find_five = find_five_mathes(original_matrix2, line, index)
#     print('find_five', find_five)
#     if find_five:
#         print('find_five', find_five)
#         pass
#     else:
#         for line, index in matched:
#             find_square = find_square_mathes(original_matrix2, line, index)
#             if find_square:
#                 print('find_square', find_square)
#                 pass
#             else:
#                 for line, index in matched:
#                     find_three = find_three_mathes_in_line(original_matrix2, line, index)
#                     if find_three:
#                         print('find_three', find_three)
#                         pass


def searching_best_match(matrix, matched):
    for line, index in matched:
        # print(line, index)
        find_five = find_five_mathes(matrix, line, index)
        print('find_five', find_five)
        if find_five is not None:
            print('есть find_five', find_five)
            return find_five

    for line, index in matched:
        find_square = find_square_mathes(matrix, line, index)
        if find_square is not None:
            print('find_square', find_square)
            return find_square

    for line, index in matched:
        find_three_line = find_three_mathes_in_line(matrix, line, index)
        if find_three_line is not None:
            print('find_three_line', find_three_line)
            return find_three_line

    for line, index in matched:
        find_three_column = find_three_mathes_in_column(matrix, line, index)
        if find_three_column is not None:
            print('find_three_column', find_three_column)
            return find_three_column




searching_best_match(original_matrix2, matched)


# Ищем совпадения по горизонтали, получаем списки с индексами второго из совпавших
# matched_list = []
# for line in range(len(original_matrix2)):
#     # print([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
#     #        and original_matrix[line][index] != 0])
#     # matched_list.append([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
#     #        and original_matrix[line][index] != 0])
#     matched = [index for (index, letter) in enumerate(original_matrix2[line])
#                if letter == original_matrix2[line][index - 1] and original_matrix2[line][index] != 0]
#     matched_list.append(matched)
#     # print('matched', matched)
#     if matched:
#         print('matched', matched)
#         for index in matched:
#             # print('matched', matched)
#             print('full index = ', line, index)
#             value = original_matrix2[line][index]
#             try:
#                 find_five_mathes(original_matrix2, line, index)
#                 find_square_mathes(original_matrix2, line, index)
#                 find_three_mathes_in_line(original_matrix2, line, index)
#             except Exception as ex:
#                 print('except', ex)
#                 pass
# print('matched_list', matched_list)













# list2 = []
# list3 = []
# for c in range(len(list)):
#   for l in range(len(list[0])):
#     list3.append(list[l][c])
#   list2.append(list3)

# print(list3)
print('---------')
# newmatrix = []
# for n,i in enumerate(list[0]):# assuming the lists are in the same length
#
#     templist =[]
#     for l in list:
#
#         templist.append(l[n])
#     print("templist: ", n, "content: ", templist)
#     newmatrix.append(templist)
#
# for i in newmatrix:
#   print(i)
#
# print('---------')
#  Создал список по столбцам!


# for i in range(len(newmatrix)):
#   print([index for (index, letter) in enumerate(newmatrix[i]) if letter == 1])