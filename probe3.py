
original_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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


priority = [2, 5]

matched_list = []
priority_list = []
for line in range(len(original_matrix)):
    matched = [index for (index, letter) in enumerate(original_matrix[line])
               if letter == original_matrix[line][index - 1] and original_matrix[line][index] != 0]
    if matched:
        print('matched', matched)
        for index in matched:
            list = []
            print('full index = ', line, index)
            value = original_matrix[line][index]
            print('value', value)
            list.append(line)
            list.append(index)

            if value in priority:
                priority_list.append(list)
            else:
                matched_list.append(list)

print('matched_list', matched_list)
print('priority_list', priority_list)
