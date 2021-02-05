
import cv2 as cv
import numpy as np
import os
import re
from PIL import Image
import pyautogui
from time import sleep, time




input = 'needles/full_window.png'


left_area = [0, 0, 100, 768]

hooks = {'yellow.png': 1,
         'blue.png': 2,
         'green.png': 3,
         'red.png': 4,
         'pink.png': 5}




def find_items(pattern_img_path, crop_img_path, threshold=0.85, debug_mode=None):
    # Table
    path_crop = os.path.join('needles', crop_img_path)
    table_img = cv.imread(path_crop, cv.IMREAD_UNCHANGED)
    path_pattern = os.path.join('needles/panel_patterns', pattern_img_path)
    pattern_img = cv.imread(path_pattern, cv.IMREAD_UNCHANGED)

    needle_w = pattern_img.shape[1]
    needle_h = pattern_img.shape[0]

    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(table_img, pattern_img, method)

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
                cv.rectangle(table_img, top_left, bottom_right, line_color, line_type)
            elif debug_mode == 'points':
                cv.drawMarker(table_img, (center_x, center_y), marker_color, marker_type)

        # if debug_mode:
        #     cv.imshow('Matches', table_img)
        #     cv.waitKey()
    return points


def find_priority(input):
    priority_list = []
    im = Image.open(input)
    a = im.crop(left_area)
    # img_width, img_height = a.size
    a.save('needles/left_panel.png', 'PNG')
    for pattern in os.listdir('needles/panel_patterns'):
        print(pattern)
    #     if pattern[pattern.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
    #         for crop in os.listdir('needles/left_panel.png'):
    #             if crop[crop.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
    #                 # print('обрабатываем', crop, 'with', pattern)
        points = find_items(pattern, 'left_panel.png', debug_mode='points')
        print(points)
        if points:
            value = hooks[pattern]
            print('value', value)
            priority_list.append(value)

    return priority_list


print(find_priority(input))