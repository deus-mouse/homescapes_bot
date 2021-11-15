import cv2 as cv
import numpy as np
import os
import re
from PIL import Image
import pyautogui
from time import sleep, time


center_x, center_y = 1763, 720
box_side = 126
crop_area = [center_x - box_side * 8, center_y - box_side * 5,  # top left
             center_x + box_side * 8, center_y + box_side * 5]  # undo right

full_screenshot_path = "full_screenshot_img.png"
path_to_crops = "D:\code\homescapes_bot\\needles\crops"

def countdown_timer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")


def cropper():
    index_x, index_y = 0, 0  # индексы секторов по вертикали и по горизонтали
    im = Image.open(full_screenshot_path)
    a = im.crop(crop_area)  # вырезаем из всего экрана только игровое поле
    # a.show()
    img_width, img_height = a.size  # считаем количество пикселей в ранее вырезанном игровом поле
    print("a.size: ", a.size)
    # a.show()
    for y in range(0, img_height, box_side):  # проходим по вертикали с шагом в клетку
        for x in range(0, img_width, box_side):  # проходим по горизонтали с шагом в клетку
            box = (x, y, x + box_side, y + box_side)  # определяем top left и undo right клетки
            b = a.crop(box)  # вырезаем эту клетку
            # b.show()
            try:
                # сохраняем отдельные нарезки
                index = '[' + str(index_y) + '][' + str(index_x) + ']'
                crop_path = os.path.join(path_to_crops, "IMG-%s.png" % index)
                b.save(crop_path, 'PNG')
            except Exception as ex:
                print('except: ', ex)
                pass
            if index_x == 15:  # если мы дойдем до края ряда, то перейдем на следующий
                index_x = 0
                index_y += 1
            else:
                index_x += 1  # продвигаемся по ряду вправо


countdown_timer()
cropper()


