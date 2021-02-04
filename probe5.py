matrix = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 4, 1, 3, 3, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 5, 1, 5, 1, 4, 3, 0, 0, 0, 0],
           [0, 0, 0, 0, 5, 4, 2, 5, 4, 3, 0, 0, 0, 0],
           [0, 0, 0, 3, 2, 3, 1, 5, 5, 1, 3, 0, 0, 0],
           [0, 0, 0, 5, 3, 3, 0, 0, 3, 3, 1, 0, 0, 0],
           [0, 0, 0, 2, 4, 4, 3, 2, 4, 1, 2, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 3, 5, 3, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 3, 3, 2, 4, 3, 2, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


newmatrix = []
for n,i in enumerate(matrix[0]):# assuming the lists are in the same length

    templist =[]
    for l in matrix:

        templist.append(l[n])
    print("templist: ",n,"content: ", templist)
    newmatrix.append(templist)

for column in newmatrix:
    print(column)


matched_list = []
for column in range(len(matrix[0])):
    # print([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
    #        and original_matrix[line][index] != 0])
    # matched_list.append([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
    #        and original_matrix[line][index] != 0])
    matched = [index for (index, letter) in enumerate(matrix[line]) if letter == newmatrix[line][index - 1]
           and newmatrix[line][index] != 0]
    matched_list.append(matched)
    # print('matched', matched)
    if matched:
        # print('matched index in line', matched)
        for index in matched:
            # print('matched', matched)
            # print('full index = ', line, index)
            value = newmatrix[line][index]
            # print('value', value)
            try:
            # Ищем совпадение на тройку в столбец
            #  ищем возможность сложить
                if newmatrix[line - 1][index - 2] == value:
                    #  совпадение top left
                    print('совпадение top left', value)
                    # нашли. двигаем сверху вниз
                    print('!!! нашли. двигаем сверху вниз')
                    move_index = [line - 1, index - 2]
                    move_index.reverse()
                    print('move_index', move_index)

                if newmatrix[line][index - 3] == value:
                    #  совпадение middle left
                    print('совпадение middle left', value)
                    # нашли. двигаем слева направо
                    print('!!! нашли. двигаем слева направо')
                    move_index = [line, index - 3]
                    move_index.reverse()
                    print('move_index', move_index)

                if newmatrix[line + 1][index - 2] == value:
                    #  совпадение lower left
                    print('совпадение lower left', value)
                    # нашли. двигаем снизу наверх
                    print('!!! нашли. двигаем снизу наверх')
                    move_index = [line + 1, index - 2]
                    move_index.reverse()
                    print('move_index', move_index)

                if newmatrix[line - 1][index + 1] == value:
                    #  совпадение top right
                    print('совпадение top right', value)
                    # нашли. двигаем сверху вниз
                    print('!!! нашли. двигаем сверху вниз')
                    move_index = [line - 1, index + 1]
                    move_index.reverse()
                    print('move_index', move_index)

                if newmatrix[line][index + 2] == value:
                    #  совпадение middle right
                    print('совпадение middle right', value)
                    # нашли. двигаем справа налево
                    print('!!! нашли. двигаем справа налево')
                    move_index = [line, index + 2]
                    move_index.reverse()
                    print('move_index', move_index)

                if newmatrix[line + 1][index + 1] == value:
                    #  совпадение lower right
                    print('совпадение lower right', value)
                    # нашли. двигаем снизу вверх
                    print('!!! нашли. двигаем снизу вверх')
                    move_index = [line + 1, index + 1]
                    move_index.reverse()
                    print('move_index', move_index)

            except Exception as ex:
                print('except', ex)
                pass

