matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
for line in range(len(newmatrix)):
    # print([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
    #        and original_matrix[line][index] != 0])
    # matched_list.append([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
    #        and original_matrix[line][index] != 0])
    matched = [index for (index, letter) in enumerate(newmatrix[line]) if letter == newmatrix[line][index - 1]
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
                    # нашли. двигаем слева направо
                    print('!!! нашли. двигаем слева направо')
                    move_index = [line - 1, index - 2]
                    print('move_index', move_index)
                    move_index.reverse()
                    print('move_index_reverse', move_index)

                if newmatrix[line][index - 3] == value:
                    #  совпадение top middle
                    print('совпадение top middle', value)
                    # нашли. двигаем сверху вниз
                    print('!!! нашли. двигаем сверху вниз')
                    move_index = [line, index - 3]
                    print('move_index', move_index)
                    move_index.reverse()
                    print('move_index_reverse', move_index)

                if newmatrix[line + 1][index - 2] == value:
                    #  совпадение top right
                    print('совпадение top right', value)
                    # нашли. двигаем справа налево
                    print('!!! нашли. двигаем справа налево')
                    move_index = [line + 1, index - 2]
                    print('move_index', move_index)
                    move_index.reverse()
                    print('move_index_reverse', move_index)

                if newmatrix[line - 1][index + 1] == value:
                    #  совпадение lower left
                    print('совпадение lower left', value)
                    # нашли. двигаем слева направо
                    print('!!! нашли. двигаем слева направо')
                    move_index = [line - 1, index + 1]
                    print('move_index', move_index)
                    move_index.reverse()
                    print('move_index_reverse', move_index)

                if newmatrix[line][index + 2] == value:
                    #  совпадение low middle
                    print('совпадение low middle', value)
                    # нашли. двигаем справа налево
                    print('!!! нашли. двигаем снизу вверх')
                    move_index = [line, index + 2]
                    print('move_index', move_index)
                    move_index.reverse()
                    print('move_index_reverse', move_index)

                if newmatrix[line + 1][index + 1] == value:
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

