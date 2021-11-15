import cv2 as cv
import numpy as np
import os
import re
from PIL import Image
import pyautogui
from time import sleep, time
from cropper import cropper

center_x, center_y = 1763, 720
box_side = 126
crop_area = [center_x - box_side * 8, center_y - box_side * 5,  # top left
             center_x + box_side * 8, center_y + box_side * 5]  # undo right

full_screenshot_path = "full_screenshot_img.png"
left_panel_img_path = 'needles/left_panel.png'

path_to_crops = "D:\code\homescapes_bot\\needles\crops"
patterns_path = 'D:\code\homescapes_bot\\needles\patterns'


area = [center_x - box_side * 7, center_y - box_side * 5,
        center_x + box_side * 7, center_y + box_side * 5]

index_pattern = '\d+\]\[\d+'
index_line_pattern = '^\d+'
index_column_pattern = '\d+$'

matrix = [[0 for i in range(16)] for i in range(10)]

hooks = {'yellow.png': 1,
         'blue.png': 2,
         'green.png': 3,
         'red.png': 4,
         'pink.png': 5,
         'fly.png': 9,
         'bomb.png': 9,
         'whirligig.png': 9}


def countdown_timer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 2):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")


def find_items(find_where, find_what, threshold=0.5, debug_mode=None):
    img_for_searching = cv.imread(find_where, cv.IMREAD_UNCHANGED)
    print(find_where)
    pattern_img = cv.imread(find_what, cv.IMREAD_UNCHANGED)
    print(find_what)

    # https://docs.opencv.org/4.5.3/d8/d6a/group__imgcodecs__flags.html
    # IMREAD_UNCHANGED = If set, return the loaded image as is (with alpha channel, otherwise it gets cropped). Ignore EXIF orientation.
    # размеры паттерна
    needle_w = pattern_img.shape[1]
    needle_h = pattern_img.shape[0]

    method = cv.TM_CCOEFF_NORMED
    # https://docs.opencv.org/4.5.1/df/dfb/group__imgproc__object.html
    result = cv.matchTemplate(img_for_searching, pattern_img, method)

    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    # Избавляемся от повторов
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, threshold)

    points = []
    if len(rectangles):
        # print('Found!')
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        # Отмечаем что нашли на столе
        for (x, y, w, h) in rectangles:
            # Определим центр объекта
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            # Сохраним точки
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
                # Определим квадраты
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # Рисуем квадраты
                cv.rectangle(img_for_searching, top_left, bottom_right, line_color, line_type)
            elif debug_mode == 'points':
                cv.drawMarker(img_for_searching, (center_x, center_y), marker_color, marker_type)

        # if debug_mode:
        #     cv.imshow('Matches', table_img)
        #     cv.waitKey()
    return points


def matrix_setter():
    # Перебираем все картинки в папке
    find = False
    for pattern in os.listdir(patterns_path):  # перебираем паттерны
        if pattern[pattern.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
            # .rfind(".") находит индекс символа,
            # +1: прием чтобы взять все след символы после найденого
            for crop in os.listdir(path_to_crops):  # перебираем сделанные ранее в методе cropper нарезки
                if crop[crop.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
                    crop_path = os.path.join(path_to_crops, crop)  # берем отдельную нарезку
                    # print("crop_path: ", crop_path)
                    pattern_path = os.path.join(patterns_path, pattern)  # берем отдельный паттерн
                    # print("pattern_path: ", pattern_path)

                    points = find_items(crop_path, pattern_path,
                                        threshold=0.70,  # играем этим значением
                                        debug_mode='points')
                    # print("points: ", points)
                    if len(points) >= 1:
                        print("crop_path: ", crop_path)
                        print("pattern_path: ", pattern_path)

                        find = True
                        index = re.search(index_pattern, crop)
                        # print('hooks[pattern]', hooks[pattern])
                        # print('index', index.group())
                        index_line = re.search(index_line_pattern, index.group())
                        index_line = index_line.group()
                        index_column = re.search(index_column_pattern, index.group())
                        index_column = index_column.group()

                        # подставляем индексу в матрице значение крючка
                        matrix[int(index_line)][int(index_column)] = hooks[pattern]
                        # print(matrix)

    # если не нашли совпадения, то нужно сместить область обзора
    # if find == False:
    #     print("если не нашли совпадения, то нужно сместить область обзора")
    #
    #     offset = 35  # на сколько нужно сместиться если число по горизонтали нечетное
    #     area[0], area[2] = area[0] - offset, area[2] - offset
    #     cropper()
    #     matrix_setter()
    #
    for line in matrix:
        print(line)
    return matrix



countdown_timer()
matrix_setter()
print("-------")
