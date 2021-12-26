matched_list = []
priority_list = []
bonus_list = []

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

for line in range(len(matrix)):
    matrix_line = matrix[line]

    if bonus_value in matrix_line:
        list = []
        index = matrix_line.index(bonus_value)
        list.append(line)
        list.append(index)
        bonus_list.append(list)

    matched = [index for (index, value)
               in enumerate(matrix[line])  # (index в текущей строке, значение)
               if value == matrix[line][index - 1] and matrix[line][index] != 0]
    if matched:
        print("matched: ", matched)
        for index in matched:
            list = []
            value = matrix[line][index]
            list.append(line)
            list.append(index)
            # если значение из списка целей
            if value in primary:
                priority_list.append(list)
            else:
                matched_list.append(list)

print("priority_list: ", priority_list)
print("matched_list: ", matched_list)
print("bonus_list: ", bonus_list)
print("-----")
for line in range(len(matrix)):
    matched = [index for (index, value) in enumerate(matrix[line])]
    print(matched)

for line in matrix:
    print(f"{line=}")



