
original_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 4, 1, 3, 3, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 5, 1, 5, 1, 4, 3, 0, 0, 0, 0],
                   [0, 0, 0, 0, 5, 4, 2, 5, 4, 3, 0, 0, 0, 0],
                   [0, 0, 0, 3, 2, 3, 1, 5, 5, 1, 3, 0, 0, 0],
                   [0, 0, 0, 5, 3, 3, 0, 0, 3, 3, 1, 0, 0, 0],
                   [0, 0, 0, 2, 4, 4, 3, 2, 4, 1, 2, 0, 0, 0],
                   [0, 0, 0, 0, 1, 1, 3, 5, 3, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 3, 3, 2, 4, 3, 2, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 9, 1, 4, 1, 3, 3, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 9, 9, 5, 1, 4, 3, 0, 0, 0, 0],
          [0, 0, 0, 6, 5, 4, 6, 7, 4, 7, 0, 0, 0, 0],
          [0, 0, 0, 6, 2, 5, 6, 5, 7, 7, 3, 0, 0, 0],
          [0, 0, 6, 8, 8, 6, 0, 6, 1, 3, 1, 0, 0, 0],
          [0, 0, 0, 8, 4, 4, 6, 2, 4, 9, 9, 0, 9, 0],
          [0, 0, 0, 6, 8, 1, 6, 5, 3, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 3, 3, 2, 4, 3, 2, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]




matched_list = []
for line in range(len(matrix)):
    # print([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
    #        and original_matrix[line][index] != 0])
    # matched_list.append([index for (index, letter) in enumerate(original_matrix[line]) if letter == original_matrix[line][index - 1]
    #        and original_matrix[line][index] != 0])
    matched = [index for (index, letter) in enumerate(matrix[line]) if letter == matrix[line][index - 1]
           and matrix[line][index] != 0]
    matched_list.append(matched)
    # print('matched', matched)
    if matched:
        print('matched index in line', matched)
        for index in matched:
            # print('matched', matched)
            print('full index = ', line, index)
            value = matrix[line][index]
            print('value', value)
            try:
            # Ищем совпадение на тройку в столбец


            #  ищем возможность сложить
            except Exception as ex:
                print('except', ex)
                pass
