import cv2 as cv
import numpy as np
import os
import re
from PIL import Image
import pyautogui
from time import sleep, time


center_x, center_y = 1763, 720
box_side = 126
game_field_area = [center_x - box_side * 8, center_y - box_side * 5,  # координаты левого верхнего угла
             box_side * 16, box_side * 10]  # кол-во пикселей по горизонтали и вертикали от top left

game_field_img_path = "game_field.png"
full_screenshot_path = "full_screenshot_img.png"

def countdown_timer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")


def take_game_field_img():
    # делает скриншот текущего состояния игрового поля
    # 3440-1440 (1720-720)
    image = pyautogui.screenshot(game_field_img_path,
                                 region=game_field_area
                                 )
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    cv.imwrite(game_field_img_path, image)


def take_full_screen():
    # делает скриншот текущего состояния игрового поля
    # 3440-1440 (1720-720)
    image = pyautogui.screenshot(full_screenshot_path)
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    cv.imwrite(full_screenshot_path, image)


countdown_timer()
take_game_field_img()
take_full_screen()


