import cv2 as cv
import numpy as np
import os
import re
import time



os.chdir(os.path.dirname(os.path.abspath(__file__)))


matrix = [[0 for i in range(14)] for i in range(10)]
print(matrix)

hooks = {'yellow.png': 1,
         'blue.png': 2,
         'green.png': 3,
         'red.png': 4,
         'pink.png': 5}

index_pattern = '\d+\]\[\d+'
index_line_pattern = '^\d+'
index_column_pattern = '\d+$'


def find_items(pattern_img_path, crop_img_path, threshold=0.5, debug_mode=None):

    # Table
    path_crop = os.path.join('needles/crops', crop_img_path)
    # print(path_crop)
    table_img = cv.imread(path_crop, cv.IMREAD_UNCHANGED)
    path_pattern = os.path.join('needles/patterns', pattern_img_path)
    # print(path_pattern)
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
    # print('rectangles', rectangles)
    # print('len', len(rectangles))

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


i = 0
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
                    # print('Found!')
                    # print('points', points)
                    # print('crop', crop)
                    # i += 1

# print(i)

for line in matrix:
    print(line)

i = 0

for l in range(len(matrix)):
    for c in range(len(matrix[0])-1):
        if matrix[l][c] == matrix[l][c+1]:
            if matrix[l][c] != 0:
                print('Found', matrix[l][c], matrix[l][c+1])
        else:
            i += 1

print('---------')

i = 0
for c in range(len(matrix[0])-1):
    for l in range(len(matrix)):
        if matrix[l][c] == matrix[l][c+1]:
            if matrix[l][c] != 0:
                print('Found', matrix[l][c], matrix[l][c+1])
        else:
            i += 1



# i = 0
# try:
#     for c in range(len(matrix[0])):
#         if matrix[c][i] == matrix[c][i+1]:
#             if matrix[c][i] == 0:
#                 pass
#             print('Found', matrix[c][i], matrix[c][i+1])
#         else:
#             i += 1
# except Exception as ex:
#     print(ex)







