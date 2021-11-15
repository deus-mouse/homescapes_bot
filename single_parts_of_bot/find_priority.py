import cv2 as cv
import numpy as np
import os
import re
from PIL import Image
import pyautogui
from time import sleep, time

full_screenshot_path = "full_screenshot_img.png"
left_panel_img_path = 'left_panel.png'
panel_patterns_path = 'D:\code\homescapes_bot\\needles\panel_patterns'


hooks = {'yellow.png': 1,
         'blue.png': 2,
         'green.png': 3,
         'red.png': 4,
         'pink.png': 5,
         'fly.png': 9,
         'bomb.png': 9,
         'whirligig.png': 9}


def find_items(find_where, find_what, threshold=0.5, debug_mode=None):
    img_for_searching = cv.imread(find_where, cv.IMREAD_UNCHANGED)
    pattern_img = cv.imread(find_what, cv.IMREAD_UNCHANGED)

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


def find_priority():
    priority_list = []
    im = Image.open(full_screenshot_path)
    a = im.crop([300, 0, 500, 1440])
    a.save(left_panel_img_path, 'PNG')
    for pattern in os.listdir(panel_patterns_path):
        priority_pattern_path = os.path.join(panel_patterns_path, pattern)
        points = find_items(find_where=left_panel_img_path, find_what=priority_pattern_path,
                                 threshold=0.85, debug_mode='points')
        if points:
            value = hooks[pattern]
            priority_list.append(value)

    return priority_list


primary = find_priority()
print('primary', primary)
