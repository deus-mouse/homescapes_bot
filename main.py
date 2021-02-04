import cv2 as cv
import numpy as np
import os
import re
from PIL import Image



os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Left panel
# searching_block_img = cv.imread('needles/base_screen.png', cv.IMREAD_UNCHANGED)
# green_cup_img = cv.imread('needles/green_cup3.png', cv.IMREAD_UNCHANGED)
#
# panel_result = cv.matchTemplate(searching_block_img, green_cup_img, cv.TM_CCOEFF_NORMED)
#
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(panel_result)
#
# print('Best match top left position: %s' % str(max_loc))
# print('Best match confidence: %s' % max_val)
# print(panel_result)
#
# threshold = 0.95
# locations1 = np.where(panel_result >= threshold)
# print('locations1', locations1)
# print('len', len(locations1))
#
# locations1 = list(zip(*locations1[::-1]))
# print('locations1', locations1)


# Определяем область зрения стола
center_x = 706
center_y = 384
box_side = 68
area = (center_x - box_side * 7, center_y - box_side * 5,
        center_x + box_side * 7, center_y + box_side * 5)

# Создали пустую матрицу
matrix = [[0 for i in range(14)] for i in range(10)]

hooks = {'yellow.png': 1,
         'blue.png': 2,
         'green.png': 3,
         'red.png': 4,
         'pink.png': 5}

index_pattern = '\d+\]\[\d+'
index_line_pattern = '^\d+'
index_column_pattern = '\d+$'

# pattern_img_path = '/Users/roman/Documents/Documents_iMac/CodeProjects/PythonProjects/Homescapes_bot/needles/patterns'
crop_img_path = '/Users/roman/Documents/Documents_iMac/CodeProjects/PythonProjects/Homescapes_bot/needles/crops'
table_img_path = 'needles/table3.png'


def cropper(path, input, height, width, area):
    index_1 = 0
    index_2 = 0
    im = Image.open(input)
    a = im.crop(area)
    img_width, img_height = a.size
    a.show()
    for i in range(0, img_height, height):
        for j in range(0, img_width, width):
            box = (j, i, j+width, i+height)
            b = a.crop(box)
            try:
                o = b.crop()
                # o.show()
                index = '[' + str(index_1) + '][' + str(index_2) + ']'
                full_path = os.path.join(path, "IMG-%s.png" % index)
                print(full_path)
                o.save(full_path, 'PNG')
                print('save')
            except Exception as ex:
                print('except', ex)
                pass
            if index_2 == 13:
                index_2 = 0
                index_1 += 1
            else:
                index_2 += 1


def find_items(pattern_img_path, crop_img_path, threshold=0.5, debug_mode=None):

    # Table
    path_crop = os.path.join('needles/crops', crop_img_path)
    table_img = cv.imread(path_crop, cv.IMREAD_UNCHANGED)
    path_pattern = os.path.join('needles/patterns', pattern_img_path)
    green_cup_on_table = cv.imread(path_pattern, cv.IMREAD_UNCHANGED)

    needle_w = green_cup_on_table.shape[1]
    needle_h = green_cup_on_table.shape[0]

    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(table_img, green_cup_on_table, method)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    # Избавляемся от повторов
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

    points = []
    if len(rectangles):
        # print('Found!')
        line_color = (0,255,0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        # Отмечаем что нашли на столе
        for (x, y, w, h) in rectangles:
            # Определим центр объекта
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # Сохраним точки
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
                # Определим квадраты
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # Рисуем квадраты
                cv.rectangle(table_img, top_left, bottom_right, line_color, line_type)
            elif debug_mode == 'points':
                cv.drawMarker(table_img, (center_x, center_y), marker_color, marker_type)

        # if debug_mode:
        #     cv.imshow('Matches', table_img)
        #     cv.waitKey()
    return points


def matrix_setter(matrix):
# Перебираем все картинки в папке
    for pattern in os.listdir('needles/patterns'):
        if pattern[pattern.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
            for crop in os.listdir('needles/crops'):
                if crop[crop.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
                    # print('обрабатываем', crop, 'with', pattern)
                    points = find_items(pattern, crop, debug_mode='points')
                    if len(points) >= 1:
                        index = re.search(index_pattern, crop)
                        # print('hooks[pattern]', hooks[pattern])
                        # print('index', index.group())
                        index_line = re.search(index_line_pattern, index.group())
                        index_line = index_line.group()
                        index_column = re.search(index_column_pattern, index.group())
                        index_column = index_column.group()
                        matrix[int(index_line)][int(index_column)] = hooks[pattern]
    return matrix


# for line in matrix_setter(matrix):
#     print(line)


def reverse_matrix(matrix):
    reverse_matrix = []
    for n, i in enumerate(matrix[0]):  # assuming the lists are in the same length
        templist = []
        for l in matrix:
            templist.append(l[n])
        reverse_matrix.append(templist)
    return reverse_matrix


def matched(matrix):
    # Ищем совпадения по горизонтали, получаем списки с индексами второго из совпавших
    matched_list = []
    for line in range(len(matrix)):
        matched = [index for (index, letter) in enumerate(matrix[line])
                   if letter == matrix[line][index - 1] and matrix[line][index] != 0]
        if matched:
            print('matched', matched)
            for index in matched:
                list = []
                print('full index = ', line, index)
                # value = matrix[line][index]
                list.append(line)
                list.append(index)
                matched_list.append(list)
    return matched_list


def find_five_mathes(matrix, line, index):
    # Ищем совпадение на 5
    value = matrix[line][index]
    try:
        if matrix[line - 1][index - 2] == value and matrix[line - 2][index - 2] == value:
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

        elif matrix[line - 1][index + 1] == value and matrix[line - 2][index + 1] == value:
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

        elif matrix[line + 1][index - 2] == value and matrix[line + 2][index - 2] == value:
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

        elif matrix[line + 1][index + 1] == value and matrix[line + 2][index + 1] == value:
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


def find_square_mathes(matrix, line, index):
    # Ищем совпадение на квадрат
    value = matrix[line][index]
    try:
        if matrix[line - 1][index - 1] == value:
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

        elif matrix[line - 1][index] == value:
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

        elif matrix[line + 1][index - 1] == value:
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

        elif matrix[line + 1][index] == value:
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


def find_three_mathes_in_line(matrix, line, index):
    value = matrix[line][index]
    try:
        # Ищем совпадение на тройку в ряд
        #  ищем возможность сложить
        if matrix[line - 1][index - 2] == value:
            #  совпадение top left
            print('совпадение top left')
            # нашли. двигаем сверху вниз
            direction = 'to down'
            move_index = [line - 1, index - 2]
            print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

        elif matrix[line][index - 3] == value:
            #  совпадение middle left
            print('совпадение middle left')
            # нашли. двигаем слева направо
            direction = 'to right'
            move_index = [line, index - 3]
            print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

        elif matrix[line + 1][index - 2] == value:
            #  совпадение lower left
            print('совпадение lower left')
            # нашли. двигаем снизу наверх
            direction = 'to up'
            move_index = [line + 1, index - 2]
            print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

        elif matrix[line - 1][index + 1] == value:
            #  совпадение top right
            print('совпадение top right')
            # нашли. двигаем сверху вниз
            direction = 'to down'
            move_index = [line - 1, index + 1]
            print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

        elif matrix[line][index + 2] == value:
            #  совпадение middle right
            print('совпадение middle right')
            # нашли. двигаем справа налево
            direction = 'to left'
            move_index = [line, index + 2]
            print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

        elif matrix[line + 1][index + 1] == value:
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


def find_three_mathes_in_column(matrix):
    rev_matrix = reverse_matrix(matrix)
    matched_list = matched(rev_matrix)

    for index, line in matched_list:
        value = matrix[line][index]
        try:
            # Ищем совпадение на тройку в столбец
            #  ищем возможность сложить
            if reverse_matrix[line - 1][index - 2] == value:
                #  совпадение top left
                print('совпадение top left', value)
                # нашли. двигаем слева направо
                move_index = [line - 1, index - 2]
                move_index.reverse()
                direction = 'to right'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if reverse_matrix[line][index - 3] == value:
                #  совпадение top middle
                print('совпадение top middle', value)
                # нашли. двигаем сверху вниз
                move_index = [line, index - 3]
                move_index.reverse()
                direction = 'to down'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if reverse_matrix[line + 1][index - 2] == value:
                #  совпадение top right
                print('совпадение top right', value)
                # нашли. двигаем справа налево
                move_index = [line + 1, index - 2]
                move_index.reverse()
                direction = 'to left'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if reverse_matrix[line - 1][index + 1] == value:
                #  совпадение lower left
                print('совпадение lower left', value)
                # нашли. двигаем слева направо
                move_index = [line - 1, index + 1]
                move_index.reverse()
                direction = 'to right'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if reverse_matrix[line][index + 2] == value:
                #  совпадение low middle
                print('совпадение low middle', value)
                # нашли. двигаем справа налево
                move_index = [line, index + 2]
                move_index.reverse()
                direction = 'to up'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            if reverse_matrix[line + 1][index + 1] == value:
                #  совпадение lower right
                print('совпадение lower right', value)
                # нашли. двигаем справа налево
                move_index = [line + 1, index + 1]
                move_index.reverse()
                direction = 'to left'
                print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

        except Exception as ex:
            print('except', ex)
            pass


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




def run(matrix):
    cropper(crop_img_path, table_img_path, 68, 68, area)
    matrix = matrix_setter(matrix)
    matched_list = matched(matrix)
    searching_best_match(matrix, matched_list)


run(matrix)
