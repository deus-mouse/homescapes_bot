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


def matched():
    priority_list_in_line=[[1, 9], [5, 6], [5, 10], [8, 6]]
    priority_list_in_column=[[5, 6], [7, 7], [8, 9], [3, 10]]
    matched_list_in_line=[[4, 9], [6, 6], [7, 6]]
    matched_list_in_column=[[3, 5], [4, 8], [3, 9], [7, 10]]
    bonus_list=[]
    return priority_list_in_line, priority_list_in_column, matched_list_in_line, matched_list_in_column, bonus_list


def find_five_matсhes_in_line(matched_list):
    # Ищем совпадение на 5
    for line, index in matched_list:

        value = matrix[line][index]
        try:
            if matrix[line - 1][index - 2] == value and matrix[line - 2][index - 2] == value \
                    and matrix[line][index - 2] != 0:
                #  совпадение top left
                #  ищем возможность сложить
                if matrix[line][index - 3] == value:
                    # нашли. двигаем слева направо
                    move_index = [line, index - 3]
                    direction = 'to right'
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                elif matrix[line + 1][index - 2] == value:
                    # нашли. двигаем снизу наверх
                    direction = 'to up'
                    move_index = [line + 1, index - 2]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            elif matrix[line - 1][index + 1] == value and matrix[line - 2][index + 1] == value \
                    and matrix[line][index + 1] != 0:
                #  совпадение top right
                print('совпадение top right')
                #  ищем возможность сложить
                if matrix[line][index + 2] == value:
                    # нашли. двигаем справа налево
                    direction = 'to left'
                    move_index = [line, index + 2]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                elif matrix[line + 1][index + 1] == value:
                    # нашли. двигаем снизу наверх
                    direction = 'to up'
                    move_index = [line + 1, index + 1]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            elif matrix[line + 1][index - 2] == value and matrix[line + 2][index - 2] == value \
                    and matrix[line][index - 2] != 0:
                #  совпадение lower left
                print('совпадение lower left')
                #  ищем возможность сложить
                if matrix[line][index - 3] == value:
                    # нашли. двигаем слева направо
                    direction = 'to right'
                    move_index = [line, index - 3]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                elif matrix[line - 1][index - 2] == value:
                    # нашли. двигаем сверху вниз
                    direction = 'to down'
                    move_index = [line - 1, index - 2]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            elif matrix[line + 1][index + 1] == value and matrix[line + 2][index + 1] == value \
                    and matrix[line][index + 1] != 0:
                #  совпадение lower right
                print('совпадение lower right')
                #  ищем возможность сложить
                if matrix[line][index + 2] == value:
                    # нашли. двигаем справа налево
                    direction = 'to left'
                    move_index = [line, index + 2]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                elif matrix[line - 1][index + 1] == value:
                    # нашли. двигаем сверху вниз
                    direction = 'to down'
                    move_index = [line - 1, index + 1]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            return move_index, direction

        except Exception as ex:
            print('except', ex)
            pass


def find_five_matches_in_column(primary):
    pass
    # TODO описать метод определения совпадения на 5 по вертикали.


def find_square_matches( line, index):
    # Ищем совпадение на квадрат
    value = matrix[line][index]
    try:
        if matrix[line - 1][index - 1] == value and matrix[line - 1][index] != 0:
            #  совпадение top left
            print('совпадение top left')
            #  ищем возможность сложить
            if matrix[line - 1][index + 1] == value:
                # нашли. двигаем справа налево
                direction = 'to left'
                move_index = [line - 1, index + 1]
                print(f'!!! нашли 4. двигаем {move_index} {direction}')
            elif matrix[line - 2][index] == value:
                # нашли. двигаем сверху вниз
                direction = 'to down'
                move_index = [line - 2, index]
                print(f'!!! нашли 4. двигаем {move_index} {direction}')
            else:
                print('не нашли возможность')

        elif matrix[line - 1][index] == value and matrix[line - 1][index - 1] != 0:
            #  совпадение top right
            print('совпадение top right')
            #  ищем возможность сложить
            if matrix[line - 1][index - 2] == value:
                # нашли. двигаем слева направо
                direction = 'to right'
                move_index = [line - 1, index - 2]
                print(f'!!! нашли 4. двигаем {move_index} {direction}')
            elif matrix[line - 2][index - 1] == value:
                # нашли. двигаем сверху вниз
                direction = 'to down'
                move_index = [line - 2, index - 1]
                print(f'!!! нашли 4. двигаем {move_index} {direction}')
            else:
                print('не нашли возможность')

        elif matrix[line + 1][index - 1] == value and matrix[line + 1][index] != 0:
            #  совпадение lower left
            print('совпадение lower left')
            #  ищем возможность сложить
            if matrix[line + 1][index + 1] == value:
                # нашли. двигаем справа налево
                direction = 'to left'
                move_index = [line - 1, index - 2]
                print(f'!!! нашли 4. двигаем {move_index} {direction}')
            elif matrix[line + 2][index] == value:
                # нашли. двигаем снизу вверх
                direction = 'to up'
                move_index = [line + 2, index]
                print(f'!!! нашли 4. двигаем {move_index} {direction}')
            else:
                print('не нашли возможность')

        elif matrix[line + 1][index] == value and matrix[line + 1][index - 1] != 0:
            #  совпадение lower right
            print('совпадение lower right')
            #  ищем возможность сложить
            if matrix[line + 1][index - 2] == value:
                # нашли. двигаем справа налево
                direction = 'to left'
                move_index = [line - 1, index - 2]
                print(f'!!! нашли 4. двигаем {move_index} {direction}')
            elif matrix[line + 2][index] == value:
                # нашли. двигаем снизу вверх
                direction = 'to up'
                move_index = [line + 2, index]
                print(f'!!! нашли 4. двигаем {move_index} {direction}')
            else:
                print('не нашли возможность')

        return move_index, direction

    except Exception as ex:
        print('except', ex)
        pass

def find_three_matches_in_line(priority_list_in_line):
    for line, index in priority_list_in_line:
        value = matrix[line][index]
        try:
            # Ищем совпадение на тройку в ряд
            #  ищем возможность сложить
            if matrix[line - 1][index - 2] == value and matrix[line][index - 2] != 0:
                #  совпадение top left
                print('совпадение top left')
                # нашли. двигаем сверху вниз
                direction = 'to down'
                move_index = [line - 1, index - 2]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif matrix[line][index - 3] == value and matrix[line][index - 2] != 0:
                #  совпадение middle left
                print('совпадение middle left')
                # нашли. двигаем слева направо
                direction = 'to right'
                move_index = [line, index - 3]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif matrix[line + 1][index - 2] == value and matrix[line][index - 2] != 0:
                #  совпадение lower left
                print('совпадение lower left')
                # нашли. двигаем снизу наверх
                direction = 'to up'
                move_index = [line + 1, index - 2]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif matrix[line - 1][index + 1] == value and matrix[line][index + 1] != 0:
                #  совпадение top right
                print('совпадение top right')
                # нашли. двигаем сверху вниз
                direction = 'to down'
                move_index = [line - 1, index + 1]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif matrix[line][index + 2] == value and matrix[line][index + 1] != 0:
                #  совпадение middle right
                print('совпадение middle right')
                # нашли. двигаем справа налево
                direction = 'to left'
                move_index = [line, index + 2]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif matrix[line + 1][index + 1] == value and matrix[line][index + 1] != 0:
                #  совпадение lower right
                print('совпадение lower right')
                # нашли. двигаем снизу вверх
                direction = 'to up'
                move_index = [line + 1, index + 1]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            return move_index, direction

        except Exception as ex:
            print('except', ex)
            pass

def find_three_matches_in_column( primary):
    rev_matrix = reverse_matrix()
    result_list = matched(rev_matrix, primary)

    try:
        for index, line in result_list[0]:
            value = rev_matrix[line][index]
            # print('value', value)
            # Ищем совпадение на тройку в столбец
            #  ищем возможность сложить
            if rev_matrix[line - 1][index - 2] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение top left
                print('совпадение top left', value)
                # нашли. двигаем слева направо
                move_index = [line - 1, index - 2]
                move_index.reverse()
                direction = 'to right'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line][index - 3] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение top middle
                print('совпадение top middle', value)
                # нашли. двигаем сверху вниз
                move_index = [line, index - 3]
                move_index.reverse()
                direction = 'to down'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line + 1][index - 2] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение top right
                print('совпадение top right', value)
                # нашли. двигаем справа налево
                move_index = [line + 1, index - 2]
                move_index.reverse()
                direction = 'to left'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line - 1][index + 1] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение lower left
                print('совпадение lower left', value)
                # нашли. двигаем слева направо
                move_index = [line - 1, index + 1]
                move_index.reverse()
                direction = 'to right'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line][index + 2] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение low middle
                print('совпадение low middle', value)
                # нашли. двигаем справа налево
                move_index = [line, index + 2]
                move_index.reverse()
                direction = 'to up'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line + 1][index + 1] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение lower right
                print('совпадение lower right', value)
                # нашли. двигаем справа налево
                move_index = [line + 1, index + 1]
                move_index.reverse()
                direction = 'to left'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

        for index, line in result_list[1]:
            value = rev_matrix[line][index]
            # print('value', value)
            # Ищем совпадение на тройку в столбец
            #  ищем возможность сложить
            if rev_matrix[line - 1][index - 2] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение top left
                print('совпадение top left', value)
                # нашли. двигаем слева направо
                move_index = [line - 1, index - 2]
                move_index.reverse()
                direction = 'to right'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line][index - 3] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение top middle
                print('совпадение top middle', value)
                # нашли. двигаем сверху вниз
                move_index = [line, index - 3]
                move_index.reverse()
                direction = 'to down'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line + 1][index - 2] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение top right
                print('совпадение top right', value)
                # нашли. двигаем справа налево
                move_index = [line + 1, index - 2]
                move_index.reverse()
                direction = 'to left'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line - 1][index + 1] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение lower left
                print('совпадение lower left', value)
                # нашли. двигаем слева направо
                move_index = [line - 1, index + 1]
                move_index.reverse()
                direction = 'to right'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line][index + 2] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение low middle
                print('совпадение low middle', value)
                # нашли. двигаем справа налево
                move_index = [line, index + 2]
                move_index.reverse()
                direction = 'to up'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if rev_matrix[line + 1][index + 1] == value and rev_matrix[line - 1][index] != 0:
                #  совпадение lower right
                print('совпадение lower right', value)
                # нашли. двигаем справа налево
                move_index = [line + 1, index + 1]
                move_index.reverse()
                direction = 'to left'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

        return move_index, direction

    except Exception as ex:
        print('except', ex)
        pass


def searching_best_match(matched, primary):
    # print('matched', matched)
    priority_list_in_line = matched[0]
    priority_list_in_column = matched[1]
    matched_list_in_line = matched[2]
    matched_list_in_column = matched[3]
    bonus_list = matched[4]

    try:
        if bonus_list != []:
            # print(line, index)
            print('find bonus!')
            direction = 'double click'
            return bonus_list, direction
            # мы могли это сделать еще раньше

        if priority_list_in_line != []:
            find_five_in_line_priority = find_five_matсhes_in_line(priority_list_in_line)
            print('find_five_in_line_priority', find_five_in_line_priority)
            if find_five_in_line_priority is not None:
                print('есть find_five_in_line_priority', find_five_in_line_priority)
                return find_five_in_line_priority

        for line, index in priority_list_in_line:
            find_square = find_square_matches(line, index)
            if find_square is not None:
                print('find_square', find_square)
                return find_square

        for line, index in priority_list_in_line:
            find_three_priority_line = find_three_matches_in_line(priority_list_in_line)
            if find_three_priority_line is not None:
                print('find_three_line', find_three_priority_line)
                return find_three_priority_line

        # for line, index in matched[0]:
        find_three_column = find_three_matches_in_column(primary)
        print('find_three_column', find_three_column)
        if find_three_column is not None:
            print('find_three_column', find_three_column)
            return find_three_column

        for line, index in matched[1]:
            # print(line, index)
            find_five = find_five_matсhes_in_line(line, index)
            print('find_five', find_five)
            if find_five is not None:
                print('есть find_five', find_five)
                return find_five

        for line, index in matched[1]:
            find_square = find_square_matches(line, index)
            if find_square is not None:
                print('find_square', find_square)
                return find_square

        for line, index in matched[1]:
            find_three_line = find_three_matches_in_line(line, index)
            if find_three_line is not None:
                print('find_three_line', find_three_line)
                return find_three_line

        # for line, index in matched[1]:
        find_three_column = find_three_matches_in_column(primary)
        print('find_three_column', find_three_column)
        if find_three_column is not None:
            print('find_three_column', find_three_column)
            return find_three_column

    except Exception as ex:
        print(ex)
        pass
