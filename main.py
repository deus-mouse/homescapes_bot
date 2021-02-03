import cv2 as cv
import numpy as np
import os




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



def find_items(needle_img_path, base_img_path, threshold=0.5, debug_mode=None):

    # Table
    table_img = cv.imread(base_img_path, cv.IMREAD_UNCHANGED)
    green_cup_on_table = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)

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
    print('rectangles', rectangles)
    print('len', len(rectangles))

    points = []
    if len(rectangles):
        print('Found!')
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

        if debug_mode:
            cv.imshow('Matches', table_img)
            cv.waitKey()

    return points

points = find_items('needles/gr_cup_table.png', 'needles/table.png', debug_mode='points')
print(points)



