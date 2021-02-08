import cv2 as cv
import numpy as np
import os
import re
from PIL import Image
import pyautogui
from time import sleep, time



def countdown_timer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")


class BotPuzzleSolver():
    def __init__(self):
        self.center_x, self.center_y = 706, 384
        self.box_side = 68
        self.area = [self.center_x - self.box_side * 7, self.center_y - self.box_side * 5,
                self.center_x + self.box_side * 7, self.center_y + self.box_side * 5]
        self.offset = 0
        self.desktop_center = [1298, 610]
        self.area_top_left_on_desktop = [self.desktop_center[0] - self.box_side * 7, self.desktop_center[1] - self.box_side * 5]

        self.path_to_crops = '/Users/roman/Documents/Documents_iMac/CodeProjects/PythonProjects/Homescapes_bot/needles/crops'
        self.full_table_img_path = 'needles/full_window.png'
        self.left_panel_img_path = 'needles/left_panel.png'
        self.panel_patterns_path = 'needles/panel_patterns'
        self.patterns_path = 'needles/patterns'

        self.DELAY_BETWEEN_LOOPS = 2.00
        self.DELAY_BETWEEN_ACTIONS = 1.00

        self.index_pattern = '\d+\]\[\d+'
        self.index_line_pattern = '^\d+'
        self.index_column_pattern = '\d+$'

        self.matrix = [[0 for i in range(14)] for i in range(10)]

        self.hooks = {'yellow.png': 1,
                 'blue.png': 2,
                 'green.png': 3,
                 'red.png': 4,
                 'pink.png': 5,
                 'fly.png': 9,
                 'bomb.png': 9,
                 'whirligig': 9}
        self.bonus_value = 9

        os.chdir(os.path.dirname(os.path.abspath(__file__)))


    def initialize_pyautogui(self):
        # Initialized PyAutoGUI
        # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
        pyautogui.FAILSAFE = True


    def take_screenshot(self):
        self.image = pyautogui.screenshot(region=(560, 202, 1365, 768))
        self.image = cv.cvtColor(np.array(self.image), cv.COLOR_RGB2BGR)
        cv.imwrite(self.full_table_img_path, self.image)


    def cropper(self):
        index_1, index_2 = 0, 0
        im = Image.open(self.full_table_img_path)
        a = im.crop(self.area)
        img_width, img_height = a.size
        # a.show()
        for i in range(0, img_height, self.box_side):
            for j in range(0, img_width, self.box_side):
                box = (j, i, j + self.box_side, i + self.box_side)
                b = a.crop(box)
                try:
                    o = b.crop()
                    # o.show()
                    index = '[' + str(index_1) + '][' + str(index_2) + ']'
                    full_path = os.path.join(self.path_to_crops, "IMG-%s.png" % index)
                    o.save(full_path, 'PNG')
                except Exception as ex:
                    print('except', ex)
                    pass
                if index_2 == 13:
                    index_2 = 0
                    index_1 += 1
                else:
                    index_2 += 1


    def find_items(self, find_where, find_what, threshold=0.5, debug_mode=None):
        img_for_searching = cv.imread(find_where, cv.IMREAD_UNCHANGED)
        pattern_img = cv.imread(find_what, cv.IMREAD_UNCHANGED)

        needle_w = pattern_img.shape[1]
        needle_h = pattern_img.shape[0]

        method = cv.TM_CCOEFF_NORMED
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


    def find_priority(self):
        self.priority_list = []
        im = Image.open(self.full_table_img_path)
        a = im.crop([0, 0, 100, 768])
        a.save(self.left_panel_img_path, 'PNG')
        for pattern in os.listdir(self.panel_patterns_path):
            priority_pattern_path = os.path.join(self.panel_patterns_path, pattern)
            points = self.find_items(find_where=self.left_panel_img_path, find_what=priority_pattern_path, threshold=0.85, debug_mode='points')
            if points:
                value = self.hooks[pattern]
                self.priority_list.append(value)

        return self.priority_list


    def matrix_setter(self):
        # Перебираем все картинки в папке
        find = False
        for pattern in os.listdir(self.patterns_path):
            if pattern[pattern.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
                for crop in os.listdir(self.path_to_crops):
                    if crop[crop.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
                        # print('обрабатываем', crop, 'with', pattern)

                        pattern_path = os.path.join(self.patterns_path, pattern)
                        crop_path = os.path.join(self.path_to_crops, crop)
                        points = self.find_items(crop_path, pattern_path, threshold=0.78, debug_mode='points')
                        if len(points) >= 1:
                            find = True
                            index = re.search(self.index_pattern, crop)
                            # print('hooks[pattern]', hooks[pattern])
                            # print('index', index.group())
                            index_line = re.search(self.index_line_pattern, index.group())
                            index_line = index_line.group()
                            index_column = re.search(self.index_column_pattern, index.group())
                            index_column = index_column.group()

                            # подставляем индексу в матрице значение крючка
                            self.matrix[int(index_line)][int(index_column)] = self.hooks[pattern]

        # если не нашли совпадения, то нужно сместить область обзора
        if find == False:
            offset = 35  # на сколько нужно сместиться если число по горизонтали нечетное
            self.area[0], self.area[2] = self.area[0] - offset, self.area[2] - offset
            self.cropper()
            self.matrix_setter(matrix)
        return self.matrix


    def reverse_matrix(self):
        self.rev_matrix = []
        for n, i in enumerate(self.matrix[0]):  # assuming the lists are in the same length
            templist = []
            for l in self.matrix:
                templist.append(l[n])
            self.rev_matrix.append(templist)
        return self.rev_matrix


    def matched(self, matrix, primary):
        # Ищем совпадения по горизонтали, получаем списки с индексами второго из совпавших
        matched_list = []
        priority_list = []
        bonus_list = []
        for line in range(len(self.matrix)):
            matrix_line = self.matrix[line]
            if self.bonus_value in matrix_line:
                list = []
                index = matrix_line.index(self.bonus_value)
                list.append(line)
                list.append(index)
                bonus_list.append(list)
            matched = [index for (index, letter) in enumerate(self.matrix[line])
                       if letter == self.matrix[line][index - 1] and self.matrix[line][index] != 0]
            if matched:
                for index in matched:
                    list = []
                    value = self.matrix[line][index]
                    list.append(line)
                    list.append(index)
                    if value in primary:
                        priority_list.append(list)
                    else:
                        matched_list.append(list)
        print('bonus_list', bonus_list)
        return priority_list, matched_list, bonus_list


    def find_five_matсhes(self, line, index):
        # Ищем совпадение на 5
        value = self.matrix[line][index]
        try:
            if self.matrix[line - 1][index - 2] == value and self.matrix[line - 2][index - 2] == value \
                    and self.matrix[line][index - 2] != 0:
                #  совпадение top left
                #  ищем возможность сложить
                if self.matrix[line][index - 3] == value:
                    # нашли. двигаем слева направо
                    move_index = [line, index - 3]
                    direction = 'to right'
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                elif self.matrix[line + 1][index - 2] == value:
                    # нашли. двигаем снизу наверх
                    direction = 'to up'
                    move_index = [line + 1, index - 2]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            elif self.matrix[line - 1][index + 1] == value and self.matrix[line - 2][index + 1] == value \
                    and self.matrix[line][index + 1] != 0:
                #  совпадение top right
                print('совпадение top right')
                #  ищем возможность сложить
                if self.matrix[line][index + 2] == value:
                    # нашли. двигаем справа налево
                    direction = 'to left'
                    move_index = [line, index + 2]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                elif self.matrix[line + 1][index + 1] == value:
                    # нашли. двигаем снизу наверх
                    direction = 'to up'
                    move_index = [line + 1, index + 1]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            elif self.matrix[line + 1][index - 2] == value and self.matrix[line + 2][index - 2] == value \
                    and self.matrix[line][index - 2] != 0:
                #  совпадение lower left
                print('совпадение lower left')
                #  ищем возможность сложить
                if self.matrix[line][index - 3] == value:
                    # нашли. двигаем слева направо
                    direction = 'to right'
                    move_index = [line, index - 3]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                elif self.matrix[line - 1][index - 2] == value:
                    # нашли. двигаем сверху вниз
                    direction = 'to down'
                    move_index = [line - 1, index - 2]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            elif self.matrix[line + 1][index + 1] == value and self.matrix[line + 2][index + 1] == value \
                    and self.matrix[line][index + 1] != 0:
                #  совпадение lower right
                print('совпадение lower right')
                #  ищем возможность сложить
                if self.matrix[line][index + 2] == value:
                    # нашли. двигаем справа налево
                    direction = 'to left'
                    move_index = [line, index + 2]
                    print(f'!!! нашли 5. двигаем {move_index} {direction}')
                elif self.matrix[line - 1][index + 1] == value:
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


    def find_square_mathes(self, line, index):
        # Ищем совпадение на квадрат
        value = self.matrix[line][index]
        try:
            if self.matrix[line - 1][index - 1] == value and self.matrix[line - 1][index] != 0:
                #  совпадение top left
                print('совпадение top left')
                #  ищем возможность сложить
                if self.matrix[line - 1][index + 1] == value:
                    # нашли. двигаем справа налево
                    direction = 'to left'
                    move_index = [line - 1, index + 1]
                    print(f'!!! нашли 4. двигаем {move_index} {direction}')
                elif self.matrix[line - 2][index] == value:
                    # нашли. двигаем сверху вниз
                    direction = 'to down'
                    move_index = [line - 2, index]
                    print(f'!!! нашли 4. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            elif self.matrix[line - 1][index] == value and self.matrix[line - 1][index - 1] != 0:
                #  совпадение top right
                print('совпадение top right')
                #  ищем возможность сложить
                if self.matrix[line - 1][index - 2] == value:
                    # нашли. двигаем слева направо
                    direction = 'to right'
                    move_index = [line - 1, index - 2]
                    print(f'!!! нашли 4. двигаем {move_index} {direction}')
                elif self.matrix[line - 2][index - 1] == value:
                    # нашли. двигаем сверху вниз
                    direction = 'to down'
                    move_index = [line - 2, index - 1]
                    print(f'!!! нашли 4. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            elif self.matrix[line + 1][index - 1] == value and self.matrix[line + 1][index] != 0:
                #  совпадение lower left
                print('совпадение lower left')
                #  ищем возможность сложить
                if self.matrix[line + 1][index + 1] == value:
                    # нашли. двигаем справа налево
                    direction = 'to left'
                    move_index = [line - 1, index - 2]
                    print(f'!!! нашли 4. двигаем {move_index} {direction}')
                elif self.matrix[line + 2][index] == value:
                    # нашли. двигаем снизу вверх
                    direction = 'to up'
                    move_index = [line + 2, index]
                    print(f'!!! нашли 4. двигаем {move_index} {direction}')
                else:
                    print('не нашли возможность')

            elif self.matrix[line + 1][index] == value and self.matrix[line + 1][index - 1] != 0:
                #  совпадение lower right
                print('совпадение lower right')
                #  ищем возможность сложить
                if self.matrix[line + 1][index - 2] == value:
                    # нашли. двигаем справа налево
                    direction = 'to left'
                    move_index = [line - 1, index - 2]
                    print(f'!!! нашли 4. двигаем {move_index} {direction}')
                elif self.matrix[line + 2][index] == value:
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


    def find_three_mathes_in_line(self, line, index):
        value = self.matrix[line][index]
        try:
            # Ищем совпадение на тройку в ряд
            #  ищем возможность сложить
            if self.matrix[line - 1][index - 2] == value and self.matrix[line][index - 2] != 0:
                #  совпадение top left
                print('совпадение top left')
                # нашли. двигаем сверху вниз
                direction = 'to down'
                move_index = [line - 1, index - 2]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif self.matrix[line][index - 3] == value and self.matrix[line][index - 2] != 0:
                #  совпадение middle left
                print('совпадение middle left')
                # нашли. двигаем слева направо
                direction = 'to right'
                move_index = [line, index - 3]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif self.matrix[line + 1][index - 2] == value and self.matrix[line][index - 2] != 0:
                #  совпадение lower left
                print('совпадение lower left')
                # нашли. двигаем снизу наверх
                direction = 'to up'
                move_index = [line + 1, index - 2]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif self.matrix[line - 1][index + 1] == value and self.matrix[line][index + 1] != 0:
                #  совпадение top right
                print('совпадение top right')
                # нашли. двигаем сверху вниз
                direction = 'to down'
                move_index = [line - 1, index + 1]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif self.matrix[line][index + 2] == value and self.matrix[line][index + 1] != 0:
                #  совпадение middle right
                print('совпадение middle right')
                # нашли. двигаем справа налево
                direction = 'to left'
                move_index = [line, index + 2]
                print(f'!!! нашли 3 горизонтально. двигаем {move_index} {direction}')

            elif self.matrix[line + 1][index + 1] == value and self.matrix[line][index + 1] != 0:
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


    def find_three_mathes_in_column(self, primary):
        rev_matrix = self.reverse_matrix()
        matched_list = self.matched(rev_matrix, primary)

        try:
            for index, line in matched_list[0]:
                value = rev_matrix[line][index]
                # print('value', value)
                # Ищем совпадение на тройку в столбец
                #  ищем возможность сложить
                if rev_matrix[line - 1][index - 2] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение top left
                    print('совпадение top left', value)
                    # нашли. двигаем слева направо
                    move_index = [line - 1, index - 2]
                    move_index.reverse()
                    direction = 'to right'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line][index - 3] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение top middle
                    print('совпадение top middle', value)
                    # нашли. двигаем сверху вниз
                    move_index = [line, index - 3]
                    move_index.reverse()
                    direction = 'to down'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line + 1][index - 2] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение top right
                    print('совпадение top right', value)
                    # нашли. двигаем справа налево
                    move_index = [line + 1, index - 2]
                    move_index.reverse()
                    direction = 'to left'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line - 1][index + 1] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение lower left
                    print('совпадение lower left', value)
                    # нашли. двигаем слева направо
                    move_index = [line - 1, index + 1]
                    move_index.reverse()
                    direction = 'to right'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line][index + 2] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение low middle
                    print('совпадение low middle', value)
                    # нашли. двигаем справа налево
                    move_index = [line, index + 2]
                    move_index.reverse()
                    direction = 'to up'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line + 1][index + 1] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение lower right
                    print('совпадение lower right', value)
                    # нашли. двигаем справа налево
                    move_index = [line + 1, index + 1]
                    move_index.reverse()
                    direction = 'to left'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')


            for index, line in matched_list[1]:
                value = rev_matrix[line][index]
                # print('value', value)
                # Ищем совпадение на тройку в столбец
                #  ищем возможность сложить
                if rev_matrix[line - 1][index - 2] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение top left
                    print('совпадение top left', value)
                    # нашли. двигаем слева направо
                    move_index = [line - 1, index - 2]
                    move_index.reverse()
                    direction = 'to right'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line][index - 3] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение top middle
                    print('совпадение top middle', value)
                    # нашли. двигаем сверху вниз
                    move_index = [line, index - 3]
                    move_index.reverse()
                    direction = 'to down'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line + 1][index - 2] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение top right
                    print('совпадение top right', value)
                    # нашли. двигаем справа налево
                    move_index = [line + 1, index - 2]
                    move_index.reverse()
                    direction = 'to left'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line - 1][index + 1] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение lower left
                    print('совпадение lower left', value)
                    # нашли. двигаем слева направо
                    move_index = [line - 1, index + 1]
                    move_index.reverse()
                    direction = 'to right'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line][index + 2] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение low middle
                    print('совпадение low middle', value)
                    # нашли. двигаем справа налево
                    move_index = [line, index + 2]
                    move_index.reverse()
                    direction = 'to up'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

                if rev_matrix[line + 1][index + 1] == value and rev_matrix[line - 1][index] != 0:
                    #  совпадение lower right
                    print('совпадение lower right', value)
                    # нашли. двигаем справа налево
                    move_index = [line + 1, index + 1]
                    move_index.reverse()
                    direction = 'to left'
                    print(f'!!! нашли 3 вертикально. двигаем {move_index} {direction}')

            return move_index, direction

        except Exception as ex:
            print('except', ex)
            pass


    def searching_best_match(self, matched, primary):
        # print('matched', matched)
        try:
            if matched[2] != []:
                # print(line, index)
                print('find bonus!')
                direction = 'double click'
                return matched[2], direction

            for line, index in matched[0]:
                # print(line, index)
                find_five = self.find_five_matсhes(line, index)
                print('find_five', find_five)
                if find_five is not None:
                    print('есть find_five', find_five)
                    return find_five

            for line, index in matched[0]:
                find_square = self.find_square_mathes(line, index)
                if find_square is not None:
                    print('find_square', find_square)
                    return find_square

            for line, index in matched[0]:
                find_three_line = self.find_three_mathes_in_line(line, index)
                if find_three_line is not None:
                    print('find_three_line', find_three_line)
                    return find_three_line

            # for line, index in matched[0]:
            find_three_column = self.find_three_mathes_in_column(primary)
            print('find_three_column', find_three_column)
            if find_three_column is not None:
                print('find_three_column', find_three_column)
                return find_three_column

            for line, index in matched[1]:
                # print(line, index)
                find_five = self.find_five_matсhes(line, index)
                print('find_five', find_five)
                if find_five is not None:
                    print('есть find_five', find_five)
                    return find_five

            for line, index in matched[1]:
                find_square = self.find_square_mathes(line, index)
                if find_square is not None:
                    print('find_square', find_square)
                    return find_square

            for line, index in matched[1]:
                find_three_line = self.find_three_mathes_in_line(line, index)
                if find_three_line is not None:
                    print('find_three_line', find_three_line)
                    return find_three_line

            # for line, index in matched[1]:
            find_three_column = self.find_three_mathes_in_column(primary)
            print('find_three_column', find_three_column)
            if find_three_column is not None:
                print('find_three_column', find_three_column)
                return find_three_column

        except Exception as ex:
            print(ex)
            pass




    def play_actions(self, best_result):
        index = best_result[0]
        direction = best_result[1]
        if direction == 'to up':
            pos_out = [self.area_top_left_on_desktop[0] + self.box_side * index[1], self.area_top_left_on_desktop[1] + self.box_side * index[0]]
            pyautogui.click(pos_out[0], pos_out[1], button='left', duration=0.25)
            pos_in = [self.area_top_left_on_desktop[0] + self.box_side * index[1], self.area_top_left_on_desktop[1] + self.box_side * (index[0] - 1)]
            sleep(self.DELAY_BETWEEN_ACTIONS)
            pyautogui.click(pos_in[0], pos_in[1], button='left', duration=0.25)

        elif direction == 'to down':
            pos_out = [self.area_top_left_on_desktop[0] + self.box_side * index[1], self.area_top_left_on_desktop[1] + self.box_side * index[0]]
            pyautogui.click(pos_out[0], pos_out[1], button='left', duration=0.25)
            pos_in = [self.area_top_left_on_desktop[0] + self.box_side * index[1], self.area_top_left_on_desktop[1] + self.box_side * (index[0] + 1)]
            sleep(self.DELAY_BETWEEN_ACTIONS)
            pyautogui.click(pos_in[0], pos_in[1], button='left', duration=0.25)

        elif direction == 'to left':
            pos_out = [self.area_top_left_on_desktop[0] + self.box_side * index[1], self.area_top_left_on_desktop[1] + self.box_side * index[0]]
            pyautogui.click(pos_out[0], pos_out[1], button='left', duration=0.25)
            pos_in = [self.area_top_left_on_desktop[0] + self.box_side * (index[1] - 1), self.area_top_left_on_desktop[1] + self.box_side * index[0]]
            sleep(self.DELAY_BETWEEN_ACTIONS)
            pyautogui.click(pos_in[0], pos_in[1], button='left', duration=0.25)

        elif direction == 'to right':
            pos_out = [self.area_top_left_on_desktop[0] + self.box_side * index[1], self.area_top_left_on_desktop[1] + self.box_side * index[0]]
            pyautogui.click(pos_out[0], pos_out[1], button='left', duration=0.25)
            pos_in = [self.area_top_left_on_desktop[0] + self.box_side * (index[1] + 1), self.area_top_left_on_desktop[1] + self.box_side * index[0]]
            sleep(self.DELAY_BETWEEN_ACTIONS)
            pyautogui.click(pos_in[0], pos_in[1], button='left', duration=0.25)

        elif direction == 'double click':
            pos_out = [self.area_top_left_on_desktop[0] + self.box_side * index[0][1], self.area_top_left_on_desktop[1] + self.box_side * index[0][0]]
            pyautogui.doubleClick(pos_out[0], pos_out[1], button='left', duration=0.25)
            # pyautogui.click(pos_out[0][0][0], pos_out[0][0][1], button='left', duration=0.25)
            # pyautogui.click(pos_out[0][0][0], pos_out[0][0][1], button='left', duration=0.25)




    def run(self):
        try:
            self.initialize_pyautogui()
            self.take_screenshot()
            self.cropper()
            self.matrix_setter()
            # for line in self.matrix:
            #     print(line)
            primary = self.find_priority()
            print('primary', primary)
            matched_list = self.matched(self.matrix, primary)
            print('matched_list', matched_list)
            best_result = self.searching_best_match(matched_list, primary)
            print('best_result', best_result)
            self.play_actions(best_result)
        except Exception as ex:
            print(ex)





countdown_timer()
bot = BotPuzzleSolver()

while True:
    bot.run()
    sleep(bot.DELAY_BETWEEN_LOOPS)