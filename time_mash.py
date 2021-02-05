import cv2
import pyautogui
import numpy as np




if matrix[line - 1][index - 2] == value and matrix[line - 2][index - 2] == value:
    #  совпадение top left
    #  ищем возможность сложить
    if matrix[line][index - 3] == value:
        if matrix[line][index - 2] == 0:
            return
            # нашли. двигаем слева направо
        move_index = [line, index - 3]
        direction = 'to right'
        print(f'!!! нашли 5. двигаем {move_index} {direction}')
    elif matrix[line + 1][index - 2] == value:
        if matrix[line][index - 2] == 0:
            pass



list = [1, 2, 3]

if 1 in list:
    if 2 in list:
        pass
